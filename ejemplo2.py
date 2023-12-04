#!/usr/bin/env python

from images import read_img, write_img, create_blank, size


def read_write():
    """Lee una imagen de un fichero y escríbela de nuevo"""

    pixels = read_img('cafe.jpg')
    write_img(pixels, 'cafe2.png')


def read_write2():
    """Lee una imagen de un fichero, y escríbela con la mitad de tamaño"""

    pixels = read_img('cafe.jpg')
    (width, height) = size(pixels)

    width2 = width // 2
    height2 = height // 2
    pixels2 = create_blank(width2, height2)
    for x in range(width2):
        for y in range(height2):
            pixels2[x][y] = pixels[x * 2][y * 2]
    write_img(pixels2, 'cafe2.gif')


def read_write4():
    """Lee una imagen de un fichero, y escríbela con el doble de tamaño"""

    pixels = read_img('cafe.jpg')
    (width, height) = size(pixels)
    width4 = width * 2
    height4 = height * 2
    pixels4 = create_blank(width4, height4)
    for x in range(width4):
        for y in range(height4):
            pixels4[x][y] = pixels[x // 2][y // 2]
    write_img(pixels4, 'cafe4.gif')


def main():
    read_write()
    read_write2()
    read_write4()


if __name__ == '__main__':
    main()
