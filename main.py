"""Simple 2D grid game prototype. Move the player with WASD to reach the goal."""
import sys

def main():
    width, height = 5, 5
    grid = [['.' for _ in range(width)] for _ in range(height)]
    player = [0, 0]
    goal = [4, 4]
    walls = {(2, 2), (1, 3), (3, 1)}
    for y, x in walls:
        grid[y][x] = '#'
    grid[goal[1]][goal[0]] = 'G'
    while True:
        grid[player[1]][player[0]] = 'P'
        for row in grid:
            print(' '.join(row))
        grid[player[1]][player[0]] = '.'
        if player == goal:
            print("You've reached the goal! Congratulations!")
            break
        cmd = input("Move (WASD) or Q to quit: ").strip().upper()
        if cmd == 'Q':
            print("Game aborted.")
            break
        moves = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
        if cmd in moves:
            dx, dy = moves[cmd]
            nx, ny = player[0] + dx, player[1] + dy
            if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in walls:
                player = [nx, ny]
        else:
            print("Invalid command.")
        print()

if __name__ == '__main__':
    main()