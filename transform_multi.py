from transforms import change_colors, rotate_colors, rotate_right, mirror, blur, grayscale, filter, crop, shift
from images import read_img, write_img
import sys


def transform():
    pixels = read_img(sys.argv[1])

    # Obtener todas las funciones y argumentos
    funcs_args = sys.argv[2:]

    for i in range(0, len(funcs_args)):
        # Iterar de 2 en 2 para obtener funciones y argumentos multiples en cualquier orden

        func = funcs_args[i]
        args = funcs_args[i + 1:]
        # Menu de funciones con los argumentos según donde vaya iterando el bucle for
        if func == "change_colors":
            pixels_old = (int(funcs_args[i + 1]), int(funcs_args[i + 2]), int(funcs_args[i + 3]))
            pixels_new = (int(funcs_args[i + 4]), int(funcs_args[i + 5]), int(funcs_args[i + 6]))
            pixels = change_colors(pixels, pixels_old, pixels_new)
        elif func == "rotate_colors":
            pixels = rotate_colors(pixels, int(funcs_args[i + 1]))
        elif func == "rotate_right":
            pixels = rotate_right(pixels)
        elif func == "mirror":
            pixels = mirror(pixels)
        elif func == "blur":
            pixels = blur(pixels)
        elif func == "grayscale":
            pixels = grayscale(pixels)
        elif func == "filter":
            pixels = filter(pixels, float(funcs_args[i + 1]), float(funcs_args[i + 2]), float(funcs_args[i + 3]))
        elif func == "crop":
            pixels = crop(pixels, int(funcs_args[i + 1]), int(funcs_args[i + 2]), int(funcs_args[i + 3]),
                          int(funcs_args[i + 4]))
        elif func == "shift":
            pixels = shift(pixels, int(funcs_args[i + 1]), int(funcs_args[i + 2]))

    write_img(pixels, sys.argv[1].split(".")[0] + "_trans." + sys.argv[1].split(".")[1])


def main():
    transform()


if __name__ == '__main__':
    main()
