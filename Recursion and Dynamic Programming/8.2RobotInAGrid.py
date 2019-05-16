'''8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits" such that
    the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
    the bottom right.'''


def getPath(grid, r, c, path):
    # base case
    # if row is negative or column is negative or cell is 'off limits'
    if r < 0 or c < 0 or not grid[r][c]:
        return False

    origin = (r == 0 and c == 0)
    # if the point is origin, one cell to the left or once cell to the top are not 'off limits'
    if (origin or getPath(grid, r-1, c, path) or getPath(grid, r, c-1, path)):
        path.append((r, c))
        return True
    return False


def getPathMemo(grid, r, c, path, failed):
    # base case
    # if row is negative or column is negative or cell is 'off limits'
    if r < 0 or c < 0 or not grid[r][c]:
        failed.append((r, c))
        return False

    origin = (r == 0 and c == 0)
    if (r, c) in path:
        return True
    elif (r, c) in failed:
        return False
     # if the point is origin, one cell to the left or once cell to the top are not 'off limits'
    elif (origin or getPathMemo(grid, r-1, c, path, failed) or getPathMemo(grid, r, c-1, path, failed)):
        path.append((r, c))
        return True
    return False


def robotInAGrid(grid):
    path, failed = [], []
    if len(grid) > 0:
        # tracing the grid backwards
        getPathMemo(grid, len(grid)-1, len(grid[0])-1, path, failed)
        #getPath(grid, len(grid)-1, len(grid[0])-1, path)
    return path


if __name__ == "__main__":
    grid = [[True, True, True], [False, True, True]]
    print(robotInAGrid(grid))
