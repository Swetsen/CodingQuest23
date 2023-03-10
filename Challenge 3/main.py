"""Coding Game: Challange 3"""


def check_winner(_moves):
    """Checks Winning Move based on the moves, passed as input."""
    rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    diags = [[1, 5, 9], [3, 5, 7]]

    for player in ['X', 'O']:
        for row in rows:
            if all(m in _moves[player] for m in row):
                return player
        for col in cols:
            if all(m in _moves[player] for m in col):
                return player
        for diag in diags:
            if all(m in _moves[player] for m in diag):
                return player

    if len(_moves['X']) + len(_moves['O']) == 9:
        return 'draw'

    return None


games = []
with open('Challenge 3/data', 'r', encoding="utf-8") as f:
    for line in f:
        moves = {'X': [], 'O': []}
        for i, move in enumerate(line.strip().split()):
            PLAYER = 'X' if i % 2 == 0 else 'O'
            moves[PLAYER].append(int(move))
            winner = check_winner(moves)
            if winner:
                games.append(winner)
                break

x_wins = games.count('X')
o_wins = games.count('O')
draws = games.count('draw')
print(x_wins)
print(o_wins)
print(draws)
print(x_wins * o_wins * draws)
