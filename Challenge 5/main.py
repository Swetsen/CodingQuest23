"""Coding Game: Challange 4"""


def display_pixel_pattern(rectangles):
    """Render squares on a screen in order to read out password"""
    pixels = [[False for _ in range(50)] for _ in range(10)]

    for rect in rectangles:
        rect = rect.split(" ")
        rect[0] = int(rect[0])
        rect[1] = int(rect[1])
        rect[2] = int(rect[2])
        rect[3] = int(rect[3])

        x_pos, y_pos, width, height = rect

        for i in range(x_pos, x_pos+width):
            for j in range(y_pos, y_pos+height):

                if pixels[j][i]:
                    pixels[j][i] = False
                else:
                    pixels[j][i] = True

    for row in pixels:
        print(''.join(['#' if pixel else '.' for pixel in row]))


f = open("data", "r", encoding="utf-8")
f = f.read()
f = f.split("\n")

print(display_pixel_pattern(f))
