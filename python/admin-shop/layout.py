import math
from config import GRID_SIZE, CENTER_EMPTY_RADIUS

def get_spiral_coords(index: int) -> tuple[int, int]:
    """
    Returns (x, y) coordinates on a grid, spiraling outwards from (0,0).
    Skips any coordinates that fall within CENTER_EMPTY_RADIUS.
    """
    x, y = 0, 0
    dx, dy = 0, -1
    current_idx = 0

    while True:
        if math.hypot(x, y) >= CENTER_EMPTY_RADIUS:
            if current_idx == index:
                return x * GRID_SIZE, y * GRID_SIZE
            current_idx += 1

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx

        x, y = x + dx, y + dy