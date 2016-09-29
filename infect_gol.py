from copy import deepcopy


def is_infected(curr_board, x, y):
    infected = y >= 0 and y < len(curr_board) and x >= 0 and \
        x < len(curr_board[y]) and curr_board[y][x] == -1
    return infected


def simulate_turn(curr_board, next_board, x, y, strength):
    infect = curr_board[y][x] <= strength and \
        (is_infected(curr_board, x - 1, y) or
         is_infected(curr_board, x, y + 1) or
         is_infected(curr_board, x + 1, y) or
         is_infected(curr_board, x, y - 1))
    if infect:
        next_board[y][x] = -1


def answer(population, x, y, strength):
    if population[y][x] <= strength:
        population[y][x] = -1
    else:
        return population
    curr_board = deepcopy(population)
    next_board = deepcopy(curr_board)
    while True:
        curr_board = deepcopy(next_board)
        next_board = deepcopy(curr_board)
        for cy in xrange(len(population)):
            for cx in xrange(len(population[cy])):
                simulate_turn(curr_board, next_board, cx, cy, strength)
        if curr_board == next_board:
            break
    return curr_board
