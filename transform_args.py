from transforms import change_colors, rotate_colors, filter, shift, crop
from images import read_img, write_img
import sys


def transform():
    funcion = sys.argv[2]
    pixels = read_img(sys.argv[1])

    if funcion == "change_colors":
        pixels_old = (int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
        pixels_new = (int(sys.argv[3]), int(sys.argv[7]), int(sys.argv[8]))
        pixels = change_colors(pixels, pixels_old, pixels_new)
    elif funcion == "rotate_colors":
        pixels = rotate_colors(pixels, int(sys.argv[3]))
    elif funcion == "filter":
        pixels = filter(pixels, float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
    elif funcion == "shift":
        pixels = shift(pixels, int(sys.argv[3]), int(sys.argv[4]))
    elif funcion == "crop":
        pixels = crop()
    else:
        print("Function not supported")

    write_img(pixels, sys.argv[1].split(".")[0] + "_trans." + sys.argv[1].split(".")[1])


def main():
    transform()


if __name__ == '__main__':
    main()
