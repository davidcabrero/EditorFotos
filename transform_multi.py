from transforms import change_colors, rotate_colors, rotate_right, mirror, blur, grayscale, filter, crop, shift
from images import read_img, write_img
import sys


def transform():
    pixels = read_img(sys.argv[1])

    # Obtener todas las funciones y argumentos
    funcs_args = sys.argv[2:]

    for i in range(0, len(funcs_args), 2): # Iterar de 2 en 2 para obtener funciones y argumentos multiples en cualquier orden

        func = funcs_args[i]
        args = funcs_args[i + 1:]

        if func == "change_colors":
            pixels = change_colors(pixels, *args)
        elif func == "rotate_colors":
            pixels = rotate_colors(pixels, *args)
        elif func == "rotate_right":
            pixels = rotate_right(pixels)
        elif func == "mirror":
            pixels = mirror(pixels)
        elif func == "blur":
            pixels = blur(pixels, *args)
        elif func == "grayscale":
            pixels = grayscale(pixels)
        elif func == "filter":
            pixels = filter(pixels, *args)
        elif func == "crop":
            pixels = crop(pixels, *args)
        elif func == "shift":
            pixels = shift(pixels, *args)
        else:
            print("Función inválida")

    write_img(pixels, sys.argv[1].split(".")[0] + "_trans." + sys.argv[1].split(".")[1])


def main():
    transform()


if __name__ == '__main__':
    main()