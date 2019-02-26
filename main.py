from random import shuffle, randrange
 
maze_size = { 'x': 8, 'y': 4 }

def make_maze(w = maze_size['x'], h = maze_size['y']):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    array = []
    for (a, b) in zip(hor, ver):
        array.append(a)
        array.append(b)
    return array

def show_me(current_position, maze, end_location):
    display_maze = []
    for item in maze: display_maze.append(item) 

    end_square = display_maze[end_location['y'] * 2 - 1][end_location['x'] - 1]
    s = list(end_square)
    s[1] = '🐁'
    display_maze[end_location['y'] * 2 - 1][end_location['x'] - 1] = "".join(s)

    current_square = display_maze[current_position['y'] * 2 - 1][current_position['x'] - 1]
    s = list(current_square)
    s[1] = '🐍'
    display_maze[current_position['y'] * 2 - 1][current_position['x'] - 1] = "".join(s)

    for row in maze:
      print("".join(row))

def generate_x_mark(maze_size):
    return {'x': 8, 'y': 4}

def find_finished(current_position, end_location):
    if current_position['x'] == end_location['x'] & current_position['y'] == end_location['y']:
        return False
    else:
        return True

def process_move(move, current_position, maze):
    if move == 'n':
        current_position['y'] -= 1
    elif move == 's':
        current_position['y'] += 1
    elif move == 'e':
        current_position['x'] += 1
    elif move == 'w':
        current_position['x'] -= 1
    else:
        print("That was an illegal move, try again")

def main():
    current_position = {'x': 1, 'y': 1}
    end_location = generate_x_mark(maze_size)
    maze = make_maze()

    while find_finished(current_position, end_location):
        print(chr(27) + "[2J") # Clears the terminal of previous input

        show_me(current_position, maze, end_location) # Show the maze

        move = input("Pick a direction ('n', 's', 'e', 'w'): ")
        if move == 'q':
            "Thanks for playing!"
            break
        else:
            process_move(move, current_position, maze)
 
if __name__ == '__main__':
    main()