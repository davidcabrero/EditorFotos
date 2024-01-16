from transforms import change_colors, rotate_colors, rotate_right, mirror, blur, grayscale, filter, crop, shift
from images import read_img, write_img
import sys


def transform():
    pixels = read_img(sys.argv[1])

    # Obtener función y argumentos
    func = sys.argv[2]
    args = sys.argv[3:]

    if func == "change_colors":
        pixels = change_colors(pixels, *args)
    elif func == "rotate_colors":
        pixels = rotate_colors(pixels, *args)

    # Obtener siguiente función y argumentos
    func = sys.argv[4]
    args = sys.argv[5:]

    if func == "blur":
        pixels = blur(pixels, *args)
    elif func == "grayscale":
        pixels = grayscale(pixels)

    func = sys.argv[6]
    args = sys.argv[7:]

    if func == "rotate_right":
        pixels = rotate_right(pixels)
    elif func == "mirror":
        pixels = mirror(pixels)

    func = sys.argv[8]
    args = sys.argv[9:]

    if func == "filter":
        pixels = filter(pixels, *args)
    elif func == "crop":
        pixels = crop(pixels, *args)

    func = sys.argv[10]
    args = sys.argv[11:]

    if func == "shift":
        pixels = shift(pixels, *args)

    write_img(pixels, sys.argv[1].split(".")[0] + "_trans." + sys.argv[1].split(".")[1])


def main():
    transform()


if __name__ == '__main__':
    main()