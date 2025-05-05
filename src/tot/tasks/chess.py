import re
import os
import sympy
import pandas as pd
import chess
from stockfish import Stockfish
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.chess import *
stockfish = Stockfish("C:\Program Files\stockfish\stockfish-windows-x86-64-avx2.exe")


# returns either False, or an updated position given the move in LAN and the FEN position
def is_legal(fen, move):
    try:
        board = chess.Board(fen)
    except ValueError:
        # bad FEN
        return False
    
    try: 
        move = chess.Move.from_uci(move)  # Convert LAN to a UCI move
        if move in board.legal_moves:  # Check if the move is legal
            board.push(move)
            #print("Move is legal!")
            return board.fen()
        else:
            return False
    except ValueError:
        # bad LAN
        return False

def sequence_is_legal(fen, move_arr):
    for move in move_arr:
        fen = is_legal(fen, move)
        if not fen:
            return False
    return fen

def is_mate(fen):
    try:
        board = chess.Board(fen)
    except ValueError:
        # bad FEN
        return False
    return board.is_checkmate()


def get_current_suggestion(y: str) -> str:
    last_line = y.strip().split('\n')[-1]
    return last_line.split('position becomes: ')[-1].split(')')[0], last_line.split('position becomes: ')[0].split(' (')[0]


#given a fen position, finds the best move to play and returns the next position with that move played
def next_pos(fen):
    try:
        stockfish.set_fen_position(fen)
        move = stockfish.get_best_move()
        stockfish.make_moves_from_current_position([move])
        return stockfish.get_fen_position()
    except:
        return False

class ChessTask(Task):
    """
    Input (x)   : a position in FEN format
    Output (y)  : a trajectory of 3 half-moves to reach checkmate
    Reward (r)  : 0 or 1, depending on whether the trajectory is correct
    Input Example: 
        4r3/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 b - - 0 35
    Output Example: 
        e8e1 g1f2 e1f1
    """
    def __init__(self, file='rt_0_800.csv'):
        """
        file: a csv file (fixed)
        """
        super().__init__()
        path = os.path.join(DATA_PATH, 'chess', file)
        self.data = list(pd.read_csv(path)['FEN'])
        self.answers = list(pd.read_csv(path)['Moves'])
        self.value_cache = {}
        
        # i have no idea what these two do
        self.steps = 4
        self.stops = ['\n'] * 4

    
    def __len__(self) -> int:
        return len(self.data)

    def get_input(self, idx: int) -> str:
        return self.data[idx]

    def get_answer(self, idx: int) -> str:
        return self.answers[idx]


    def test_output(self, idx: int, output: str):
        # given an output, take the last line, make it lowercase, 
        # split to array with the LAN moves
        moves = output.strip().split('\n')[-1].lower().replace('answer: ', '').split()
        
        solution = self.answers[idx]
        old_position = self.data[idx]

        # for our purposes: are there 3/4 moves, are the moves legal, and is the king in checkmate
        # depends on tuddy's design decision of whether to include og move in position or not
        if len(moves) != 3:
            return {'r': 0}
        board = sequence_is_legal(old_position, moves)
        if not board:            
            return {'r': 0}
        if not is_mate(board):
            return {'r': 0}
        solution = solution.split()
        correct = int(solution == moves)
        return {'r': correct}
            
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        return cot_prompt.format(input=x) + y
    
    @staticmethod
    def propose_prompt_wrap(x: str, y: str='') -> str:
        sugg = get_current_suggestion(y if y else x)
        current_position, current_move = sugg
        
        # im not sure chatgpt will generate the correct fen given the old fen and a move suggestion
        # so will use computed fen but will keep track of how often chat is correct
        with open("can_chat_gen_fen.txt", "w") as f:
            should_be = is_legal(x, current_move)
            if current_position == should_be:
                print("yes", file=f)    
            else:
                print("no", file=f)
                if should_be:
                    current_position = should_be

        if is_mate(current_position):
            prompt = cot_prompt.format(input=x) + 'Steps:' + y
        # print([prompt])
        else:
        #get the stockfish best response before asking to resuggest
            current_position = next_pos(current_position)
            prompt = propose_prompt.format(input=current_position)
        return prompt
    
    @staticmethod
    def value_prompt_wrap(x: str, y: str) -> str:
        last_line = y.strip().split('\n')[-1]
        if 'position becomes: ' not in last_line:  # last step
            ans = last_line.lower().replace('answer: ', '')
            # print([value_last_step_prompt.format(input=x, answer=ans)])
            return value_last_step_prompt.format(input=x, answer=ans)
        
        
        sugg = get_current_suggestion(y)
        current_position, current_move = sugg
        
        # im not sure chatgpt will generate the correct fen given the old fen and a move suggestion
        # so will use computed fen but will keep track of how often chat is correct
        with open("can_chat_gen_fen2.txt", "w") as f:
            should_be = is_legal(x, current_move)
            if current_position == should_be:
                print("yes", file=f)    
            else:
                print("no", file=f)
                if should_be:
                    current_position = should_be

        return value_prompt.format(input=current_position)
    
    @staticmethod
    def value_outputs_unwrap(x: str, y: str, value_outputs: list) -> float:
        if len(y.strip().split('\n')) == 4 and 'answer' not in y.lower():
            return 0
        value_names = [_.split('\n')[-1] for _ in value_outputs]
        value_map = {'impossible': 0.001, 'likely': 1, 'sure': 20}
        value = sum(value * value_names.count(name) for name, value in value_map.items())
        return value