def IsInRange(x, y):
    return (x>0&&x<Range)&&(y>0&&y<Range)

def search(x, y):
    Land[x][y] = 0;
    ax = [0, 1, 1, 1, 0, -1, -1, -1];
    ay = [1, 1, 0, -1, -1, -1, 0, 1];

    for i in range(8):
        dx = ax[i];
        dy = ay[i];

    if IsInRange(dx, dy) && Land[x][y] > 0:
        search(dx, dy);

