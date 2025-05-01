# src/tot/prompts/mate1.py
# Prompts for the Mate-in-One task. Each template uses {input} and, where relevant, {answer}.

# 3-shot standard prompt: give examples of FEN → solution SAN
standard_prompt = '''Here are some chess puzzles and their mate-in-one solutions.
Position (FEN): r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
Answer: Nf3#
Position (FEN): 8/8/8/1k6/8/8/5Q2/1K6 w - - 0 1
Answer: Qf2#
Position (FEN): r4rk1/pp3ppp/2n1b3/q1pp2B1/8/P1Q2NP1/1PP1PP1P/2KR3R w - - 0 1
Answer: Bd8#
Position (FEN): {input}
Answer:'''  

# 3-shot Chain-of-Thought prompt: walk through reasoning then answer
cot_prompt = '''Solve each mate-in-one puzzle step by step.

Position (FEN): r1bqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
Steps:
1. The knight on g1 can move to f3, covering h4 and d4.
2. Nf3# delivers checkmate.
Answer: Nf3#

Position (FEN): 8/8/8/1k6/8/8/5Q2/1K6 w - - 0 1
Steps:
1. The queen on f1 moves to f2, covering g3 and e3.
2. Qf2# delivers checkmate.
Answer: Qf2#

Position (FEN): {input}
Steps:'''  

# 1-shot propose prompt: list candidate SAN moves for mate-in-one
propose_prompt = '''Given the chess position (FEN): {input}
List all moves (in SAN) that deliver checkmate in one, separated by commas.'''  

# Value prompt: ask if a candidate move is a valid mate-in-one
value_prompt = '''Evaluate this candidate move for mate-in-one.
Position (FEN): {input}
Candidate move: {answer}
Does this move deliver checkmate in one? Answer TRUE or FALSE.'''  

# Last-step value prompt (if needed): judge the final answer
value_last_step_prompt = '''Check if the provided move solves the puzzle.
Position (FEN): {input}
Answer: {answer}
Judge: (sure/impossible)'''  
