# 5-shot
first_out = '''Find the mate in 2 moves.
Input: 4r3/1k6/pp3r2/1b2P2p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35
Answer: e5f6 e8e1 g1f2 e1f1
Input: r1bqk2r/pp1nbNp1/2p1p2p/8/2BP4/1PN3P1/P3QP1P/3R1RK1 b kq - 0 19
Answer: e8f7 e2e6 f7f8 e6f7
Input: 4r1k1/5ppp/r1p5/p1n1RP2/8/2P2N1P/2P3P1/3R2K1 b - - 0 21
Answer: e8e5 d1d8 e5e8 d8e8
Input: 5r1k/pp4pp/5p2/1BbQp1r1/6K1/7P/1PP3P1/3R3R w - - 2 26
Answer: g4h4 c5f2 g2g3 f2g3
Input: 1rb2rk1/q5P1/4p2p/3p3p/3P1P2/2P5/2QK3P/3R2R1 b - - 0 29
Answer: f8f7 c2h7 g8h7 g7g8q
Input: {input}
'''
#6k1/5ppp/5nb1/pp6/6rP/5N1Q/Pq2r1P1/3R2RK b - - 4 32,g6e4 d1d8 f6e8 d8e8


first_in_ish = '''
Find the mate in 2 moves. Give your final answer in LAN notation.
Input: 4r3/1k6/pp3r2/1b2P2p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35, white plays e5f6
Answer: e8e1 g1f2 e1f1
Input: r1bqk2r/pp1nbNp1/2p1p2p/8/2BP4/1PN3P1/P3QP1P/3R1RK1 b kq - 0 19, black plays e8f7
Answer: e2e6 f7f8 e6f7
Input: 4r1k1/5ppp/r1p5/p1n1RP2/8/2P2N1P/2P3P1/3R2K1 b - - 0 21, black plays e8e5
Answer: d1d8 e5e8 d8e8
Input: 5r1k/pp4pp/5p2/1BbQp1r1/6K1/7P/1PP3P1/3R3R w - - 2 26, white plays g4h4
Answer: c5f2 g2g3 f2g3
Input: 1rb2rk1/q5P1/4p2p/3p3p/3P1P2/2P5/2QK3P/3R2R1 b - - 0 29, black plays f8f7
Answer: c2h7 g8h7 g7g8q
Input: {input}

'''
#6k1/5ppp/5nb1/pp6/6rP/5N1Q/Pq2r1P1/3R2RK b - - 4 32, black plays g6e4
# d1d8 f6e8 d8e8


standard_prompt = '''
Find the mate in 2. Give your answer at the very end, in LAN notation.
Input: 4r3/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 b - - 0 35
Answer: e8e1 g1f2 e1f1
Input: r1bq3r/pp1nbkp1/2p1p2p/8/2BP4/1PN3P1/P3QP1P/3R1RK1 w - - 0 19
Answer: e2e6 f7f8 e6f7
Input: 6k1/5ppp/r1p5/p1n1rP2/8/2P2N1P/2P3P1/3R2K1 w - - 0 21
Answer: d1d8 e5e8 d8e8
Input: 5r1k/pp4pp/5p2/1BbQp1r1/7K/7P/1PP3P1/3R3R b - - 2 26
Answer: c5f2 g2g3 f2g3
Input: 1rb3k1/q4rP1/4p2p/3p3p/3P1P2/2P5/2QK3P/3R2R1 w - - 0 29
Answer: c2h7 g8h7 g7g8q
Input: {input}

'''

# 6k1/5ppp/5n2/pp6/4b1rP/5N1Q/Pq2r1P1/3R2RK w - - 4 32
# d1d8 f6e8 d8e8



# 5-shot
cot_prompt = '''Find the mate in 2. Give your answer at the very end, in LAN notation. At each step, you are only allowed to choose one piece to move to a square to obtain a new position.
Input: 4r3/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 b - - 0 35
Steps:
The opponent's king is exposed on the back rank, so we deliver a check with the rook: Re1+
The opponent can only move his king to f2: Kf2
The rook checks the king supported by the bishop, and the king has no escape squares: Rf1#
Answer: e8e1 g1f2 e1f1


Input: r1bq3r/pp1nbkp1/2p1p2p/8/2BP4/1PN3P1/P3QP1P/3R1RK1 w - - 0 19
Steps:
The pawn on e6 is only defended by the king and can be taken by the queen supported by the bishop: Qe6+
The king moves back to the back rank: Kf8
The queen checks the king supported by the bishop, and the king has no escape squares: Qf7#
Answer: e2e6 f7f8 e6f7

Input: 6k1/5ppp/r1p5/p1n1rP2/8/2P2N1P/2P3P1/3R2K1 w - - 0 21
Steps:
The opponent's king is exposed on the back rank, so we deliver a check with the rook: Rd8+
The opponent's only move is to cover with their rook: Re8
The rook takes the opponent's rook and delivers checkmate: Rxe8#
Answer: d1d8 e5e8 d8e8

Input: 5r1k/pp4pp/5p2/1BbQp1r1/7K/7P/1PP3P1/3R3R b - - 2 26
Steps:
The opponent's king has no legal moves, so we deliver a check with the bishop: Bf2#
The opponent's only move is to block the check with their pawn: g3
The bishop takes the opponent's pawn, supported by the rook, and delivers checkmate: Bxg3#
c5f2 g2g3 f2g3

Input: 1rb3k1/q4rP1/4p2p/3p3p/3P1P2/2P5/2QK3P/3R2R1 w - - 0 29
Steps:
The opponent's king is the only piece stopping our pawn on g7 from promoting, so we deflect the king with our queen: Qh7+
The opponent's only move is to take our queen: Kxh7
The pawn promotes to queen with checkmate because the opponent king has no moves: g8=Q#
Answer: c2h7 g8h7 g7g8q

Input: {input}
'''
# 6k1/5ppp/5n2/pp6/4b1rP/5N1Q/Pq2r1P1/3R2RK w - - 4 32
# d1d8 f6e8 d8e8


propose_prompt = '''Input: 4r3/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 b - - 0 35
Possible next steps:
e8f8 (position becomes: 5r2/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35)
a6a5 (position becomes: 4r3/1k6/1p3P2/pb5p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35)
b5e2 (position becomes: 4r3/1k6/pp3P2/7p/3R1p2/P1R2P2/1P2b1PP/6K1 w - - 0 35)
b7a8 (position becomes: k3r3/8/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35)
h5h4 (position becomes: 4r3/1k6/pp3P2/1b6/3R1p1p/P1R2P2/1P4PP/6K1 w - - 0 35)
e8e6 (position becomes: 8/1k6/pp2rP2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 w - - 0 35)
e8e1 (position becomes : 8/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/4r1K1 w - - 0 35)
e8e3 (position becomes: 8/1k6/pp3P2/1b5p/3R1p2/P1R1rP2/1P4PP/6K1 w - - 0 35)
Input: {input}
Possible next steps:
'''
# 6k1/5ppp/5n2/pp6/4b1rP/5N1Q/Pq2r1P1/3R2RK w - - 4 32
# d1d8 f6e8 d8e8

value_prompt = '''Evaluate whether you have a checkmate coming in the following positions. (sure/likely/impossible). The last sentence in your output is Answer: sure or Answer: likely or Answer: impossible.
Input: 5r1k/pp4pp/5p2/1B1Qp1r1/7K/6PP/1PP2b2/3R3R b - - 2 26
Finding checks: Bxg3#
Answer: sure

Input: 3Rr1k1/5ppp/r1p5/p1n2P2/8/2P2N1P/2P3P1/6K1 w - - 0 21
Finding checks: Rxe8#
Answer: sure

Input: 1rb5/q4rPk/4p2p/3p3p/3P1P2/2P5/3K3P/3R2R1 w - - 0 29
Finding checks: f5 exf5 is not mate in 1
c4 dxc4 is not mate in 1
I can't find mate now, but the opponent's king has one legal move
Answer: likely

Input: 8/6k1/bq5p/1r1p1R1p/3P4/2PK4/7P/8 w - - 0 29
Finding checks: Rg5+ hxg5 is not mate in 1
Rf7+ Kxf7 is not mate in 1
I have no checks left and I am down material
Answer: impossible

Input: 4r3/1k6/pp3P2/1b5p/3R1p2/P1R2P1P/1P4P1/6K1 b - - 0 35
Finding checks: Re1+ Kh2 is not mate in 1
Bf1 Kxf1 is not mate in 1
None of the available checks result in a checkmate
Answer: impossible

Input: {input}
Finding checks:
Answer:
'''
#6k1/5ppp/5n2/pp6/4b1rP/5N1Q/Pq2r1P1/3R2RK w - - 4 32


value_last_step_prompt = '''Find mate in 2 in the position. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. the moves are all legal and the sequence ends with a checkmate, meaning the opponent's king is in check and has no legal moves. The last sentence in your output is Verdict: sure or Verdict: impossible.
Input: 4r3/1k6/pp3P2/1b5p/3R1p2/P1R2P2/1P4PP/6K1 b - - 0 35
Answer: e8e1 g1f2 e1f1
Judge: Moves are legal and the sequence ends with a checkmate
Verdict: sure

Input: r1bq3r/pp1nbkp1/2p1p2p/8/2BP4/1PN3P1/P3QP1P/3R1RK1 w - - 0 19
Answer: e2e6 f7f8 e6f7
Judge: Moves are legal and the sequence ends with a checkmate
Verdict: sure

Input: 5r1k/pp4pp/5p2/1BbQp1r1/7K/7P/1PP3P1/3R3R b - - 2 26
Answer: f5f4 h4g5 h7h6
Judge: The opponent's king still has legal moves
Verdict: impossible

Input: 5r1k/pp4pp/5p2/1BbQp1r1/7K/7P/1PP3P1/3R3R b - - 2 26
Answer: h7h6 d5d8 f8f4 
Judge: f8f4 is an illegal move
Verdict: impossible


Input: {input}
Answer: {answer}
Judge:
Verdict:'''

# 6k1/5ppp/5n2/pp6/4b1rP/5N1Q/Pq2r1P1/3R2RK w - - 4 32
# d1d8 f6e8 d8e8