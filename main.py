from random import shuffle, randrange
 
def make_maze(w = 8, h = 4):
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

def show_me(current_position, maze):
    current_square = maze[current_position[1] * 2 - 1][current_position[0]]
    s = list(current_square)
    s[1] = '🐍'
    maze[current_position[1] * 2 - 1][current_position[0]] = "".join(s)

    for row in maze:
      print("".join(row))

def main():
    current_position = [0,1]
    maze = make_maze()
    # for row in maze:
    #   print(row)
    show_me(current_position, maze)
 
if __name__ == '__main__':
    main()