from PIL import Image


def size(pixels_xy: list[list[tuple[int, int, int]]]) -> tuple[int, int]:
    """Devuelve el tamaño de una imagen, dada una lista de listas de pixels.
    Cada elemento del array(pixel) es una tupla, en formato(R, G, B).
    Devuelve una tupla (width, height).
    """

    width = len(pixels_xy)
    height = len(pixels_xy[0])
    return (width, height)


def read_img(filename: str) -> list[list[tuple[int, int, int]]]:
    """Lee una imagen de un fichero, y devuelve un array (lista de listas) de pixels.
    Cada elemento del array (pixel) es una tupla, en formato (R, G, B).
    """

    img = Image.open(filename)
    width, height = img.size

    pixels = img.getdata()
    pixels_xy = []
    for x in range(width):
        pixels_xy.append([0] * height)
        for y in range(height):
            pixels_xy[x][y] = pixels[(y * width) + x]
    return pixels_xy


def write_img(pixels_xy: list[list[tuple[int, int, int]]], filename: str) -> None:
    """Escribe un array (lista de listas) de pizels en un fichero
    Cada elemento del array (pixel) es una tupla, en formato (R, G, B).
    """

    (width, height) = size(pixels_xy)
    pixels = [0] * width * height
    for x in range(width):
        for y in range(height):
            pixels[(y * width) + x] = pixels_xy[x][y]

    img = Image.new(mode='RGB', size=(width, height))
    img.putdata(pixels)
    img.save(filename)


def create_blank(width: int, height: int) -> list[list[tuple[int, int, int]]]:
    """Crea una imagen vacía, dada una anchura y una altura.
    Devuelve una lista de listas de pixels.
    """

    pixels = []
    for x in range(width):
        pixels.append([(0, 0, 0)] * height)
    return pixels
