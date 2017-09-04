import sys;

def bfsSearch(board, source, destination, l):
    queue = [];
    cur = 0;

    xDirection = [0, 1, 1, 1, 0, -1, -1, -1];
    yDirection = [1, 1, 0, -1, -1, -1, 0, 1];

    queue.append(source);

    xDestination, yDestination = map(int, destination);

    xInitial, yInitial = map(int, source);
    board[xInitial][yInitial] = -1;

    while queue:
        xCurrent, yCurrent = map(int, queue.pop(0));

        for i in range(8):
            xNext = xCurrent + xDirection[i];
            yNext = yCurrent + yDirection[i];

            if (xNext >= 0 and xNext < l) and (yNext >= 0 and yNext < l):
                if board[xNext][yNext] != -1:
                    board[xNext][yNext] = board[xCurrent][yCurrent] - 1;
                    queue.append([xNext, yNext]);

            if xNext == xDestination and yNext == yDestination:
                print(abs(board[xNext][yNext]));
                return;

def main():
    l = int(input());

    board = [[0 for value in range(l)] for value in range(l)];

    xSource, ySource = map(int, input().split());
    xDestination, yDestination = map(int, input().split());

    bfsSearch(board, [xSource, ySource], [xDestination, yDestination], l);

if __name__ == "__main__":
    sys.exit(int(main() or 0))
