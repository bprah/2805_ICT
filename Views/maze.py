from random import shuffle, randrange
import re

def create_maze():

    width = 9
    height = 15

    vis = [[0] * width + [1] for _ in range(height)] + [[1] * (width + 1)]
    vertical = [["1  "] * width + ['1'] for _ in range(height)] + [[]]
    horizontal = [["111"] * width + ['1'] for _ in range(height + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: horizontal[max(y, yy)][x] = "1  "
            if yy == y: vertical[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(width), randrange(height))

    s = ""
    for (a, b) in zip(horizontal, vertical):
        s += ''.join(a + ['\n'] + b + ['\n'])

    # String Manipulation - Replacing spaces with coins
    s = re.sub("[^\S\r\n]", "C", s)
    Player_pos = s.find("C")
    # Insertion of Player Character at first coin position
    s = s[:Player_pos] + "P" + s[Player_pos + 1:]

    # Addition of the enemies
    result = [_.start() for _ in re.finditer("C", s)]
    x = (len(result) //4)
    s = s[:result[x]] + "2" + s[result[x] + 1:]
    x = x + (len(result) //4)
    s = s[:result[x]] + "3" + s[result[x]+ 1:]
    x = x + (len(result) // 4)
    s = s[:result[x]] + "4" + s[result[x] + 1:]
    result = [_.start() for _ in re.finditer("C", s)]
    x = len(result) - 1
    s = s[:result[x]] + "5" + s[result[x] + 1:]


    with open("random_maze.txt", "w") as text_file:
        print(f" {s}", file=text_file)
    return


if __name__ == '__main__':
    create_maze()


    # Find
    #print(s.count("C"))
