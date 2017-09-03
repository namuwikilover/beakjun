import sys;

def bfsSearch(maze, N, M):
    queue = [];
    cur = 0;

    xDirection = [0, 1, 0, -1];
    yDirection = [1, 0, -1, 0];

    queue.append([0, 0]);
    maze[0][0] = -1;

    while queue:
        xCurrent, yCurrent = map(int, queue.pop(0));

        for i in range(4):
            xNext = xCurrent + xDirection[i];
            yNext = yCurrent + yDirection[i];

            if (xNext >= 0 and xNext < N) and (yNext >= 0 and yNext < M):
                if maze[xNext][yNext] == 1:
                    maze[xNext][yNext] = maze[xCurrent][yCurrent] - 1;
                    queue.append([xNext, yNext]);

            if xNext == N-1 and yNext == M-1:
                print(abs(maze[xNext][yNext]));
                return;

    print(maze)

def main():
    N, M = map(int, input().split())

    l = []

    for i in range(N):
        l.append(list(map(int, input())))

    #print(l)

    bfsSearch(l, N, M);
    
if __name__ == "__main__":
    sys.exit(int(main() or 0))
