def bfs(start, maze):
    queue = [];
    cur = 0;

    xDirection = [0, 1, 0, -1];
    yDirection = [-1, 0, -1, 0];

    queue.append([0, 0]);
    matrix[0][0] = -1;

    while queue:
        xCurrent, yCurrent = map(int, queue.pop(0));

        for i in range(4):
            xNext = xCurrent + xDirection[i];
            yNext = yCurrent + yDirection[i];

            if (xNext > 0 and xNext < N) and (yNext > 0 and yNext < M):
                maze[xNext][yNext] = maze[xCurrent][yCurrent] - 1;

            if nextDx==N and nextDy == M:
                print('Found!!!');
                break;

            queue.append([xNext, yNext]);

def main():
    N, M = map(int, input().split())

    l = []

    for i in range(N):
        l.append(input())
    
if __name__ == "__main__":
    sys.exit(int(main() or 0))
