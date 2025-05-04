import json, sys, re
import sympy as sp

def is_correct(expr: str) -> bool:
    """
    Given a string like '(4 + 8) * (6 - 4)', return True if it simplifies to 24.
    """
    try:
        print('expression: ', expr)
        return sp.simplify(expr) == 24
    except Exception:
        return False

def main(log_path):
    data = json.load(open(log_path, 'r', encoding='utf-8'))
    total = len(data)
    correct = 0

    for entry in data:
        ys = entry.get('ys', [])
        if not ys:
            continue
        # Take the last line of the final output
        last_line = ys[-1].strip().split('\n')[-1]
        # Remove any leading 'Answer:' and split off the '= 24' part
        # e.g. "Answer: (4 + 8) * (6 - 4) = 24"
        expr = last_line
        # Strip off 'Answer:' if present
        expr = re.sub(r'^[Aa]nswer:\s*', '', expr)
        # Take everything before the '='
        expr = expr.split('=')[0].strip()

        if is_correct(expr):
            correct += 1

    accuracy = correct / total if total else 0
    print(f"Puzzles: {total}, Solved: {correct}")
    print(f"Accuracy: {accuracy:.2%} ({correct}/{total})")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python compute_game24_accuracy.py")
        sys.exit(1)
    main('gpt-4o-mini_0.7_propose1_value3_greedy5_start900_end1000.json')
