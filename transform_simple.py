from transforms import rotate_right, mirror, blur, grayscale
from images import read_img, write_img
import sys


def transform():
    funcion = sys.argv[2]
    pixels = read_img(sys.argv[1])

    if funcion == "rotate_right":
        pixels = rotate_right(pixels)
    elif funcion == "mirror":
        pixels = mirror(pixels)
    elif funcion == "blur":
        pixels = blur()
    elif funcion == "grayscale":
        pixels = grayscale(pixels)
    else:
        print("Función no soportada")
        sys.exit()

    write_img(pixels, sys.argv[1].split(".")[0] + "_trans." + sys.argv[1].split(".")[1])


def main():
    transform()


if __name__ == '__main__':
    main()
