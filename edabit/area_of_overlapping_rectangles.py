from typing import List


def overlapping_rectangles(rectangle1: List, rectangle2: List) -> int:
    # rect = [x, y, width, height]
    overlap_width = 0
    overlap_height = 0
    x1, y1, w1, h1 = rectangle1
    left1 = x1
    right1 = x1 + w1
    bottom1 = y1
    top1 = y1 + h1

    x2, y2, w2, h2 = rectangle2
    left2 = x2
    right2 = x2 + w2
    bottom2 = y2
    top2 = y2 + h2

    overlap_left = max(left1, left2)
    overlap_right = min(right1, right2)
    overlap_top = min(top1, top2)
    overlap_bottom = max(bottom1, bottom2)

    if overlap_left < overlap_right and overlap_bottom < overlap_top:
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_top - overlap_bottom

    return overlap_width * overlap_height


print(overlapping_rectangles([2, 1, 3, 4], [3, 2, 2, 5]))
print(overlapping_rectangles([2, -9, 11, 5], [5, -11, 2, 9]))
print(overlapping_rectangles([-8, -7, 4, 7], [-5, -9, 4, 7]))
