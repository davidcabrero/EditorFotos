def change_colors(image: list[list[tuple[int, int, int]]],
                  to_change: tuple[int, int, int],
                  to_change_to: tuple[int, int, int]) -> list[list[tuple[int, int, int]]]:
    for columna in image:
        for pixel in range(len(columna)):
            if columna[pixel] == to_change:  # Sustituye el pixel si coincide con el color a cambiar
                columna[pixel] = to_change_to
    return image


def rotate_right(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    imagen = []
    aux = []
    for i in range(1, len(image[1]) + 1, 1):
        for columna in image:
            aux.append(columna[-1 * i])
        imagen.append(aux)
        aux = []
    return imagen


def mirror(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    imagen = []
    for pixel in image[::-1]:  # Recorre la imagen desde el final al inicio
        imagen.append(pixel)
    return imagen


def rotate_colors(image: list[list[tuple[int, int, int]]], increment: int) -> list[list[tuple[int, int, int]]]:
    for columna in image:
        for pixel in range(len(image[0])):
            columna[pixel] = list(columna[pixel])  # Crea lista con los pixeles
            for valor in range(0, 3):
                b = columna[pixel][valor] + increment  # Incrementa el color
                if not 0 < b < 255:  # Los valores RGB deben estar entre 0 y 255
                    b = b % 255
                columna[pixel][valor] = b
            columna[pixel] = tuple(columna[pixel])
    return image


def blur():
    ...


def greyscale():
    ...


def shift():
    ...
