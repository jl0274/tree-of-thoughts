import csv
from tot.tasks.base import Task, DATA_PATH

class MateInOneTask(Task):
    def __init__(self, file="mate1_only.csv"):
        super().__init__()
        path = DATA_PATH / "mate1" / file
        self.inputs = []     # list of (fen, san)
        with open(path) as f:
            for fen, san in csv.reader(f):
                self.inputs.append((fen, san))
        self.value_cache = {}
        self.steps = 1       # just one generation step
        self.stops = [None]  # no forced stop token

    def __len__(self):
        return len(self.inputs)

    def get_input(self, idx):
        # return the FEN; model will generate the move
        return self.inputs[idx][0]

    def test_output(self, idx, output):
        # check whether the generated SAN is exactly the gold mate
        gold = self.inputs[idx][1].strip()
        guess = output.strip().split()[-1]
        return {"r": 1 if guess == gold else 0}

    @staticmethod
    def standard_prompt_wrap(fen, _: str="") -> str:
        return (
            f"You are given a chess position (FEN):\n{fen}\n"
            "White to move. Find the single move that delivers checkmate in one. "
            "Answer with the move in SAN (e.g. Qh7#)."
        )

    @staticmethod
    def cot_prompt_wrap(fen, _: str="") -> str:
        return (
            f"Here is a chess position:\n{fen}\n"
            "Walk through your reasoning step-by-step, then give the mate-in-one move."
        )

    @staticmethod
    def value_prompt_wrap(fen, move, __=None) -> str:
        return (
            f"Position: {fen}\n"
            f"Candidate move: {move.strip()}\n"
            "Does this move deliver mate in one? TRUE or FALSE."
        )

    @staticmethod
    def value_outputs_unwrap(fen, move, value_outputs):
        answer = value_outputs[0].strip().lower()
        return 1.0 if answer.startswith("true") else 0.0
