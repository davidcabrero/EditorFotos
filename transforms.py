def change_colors(image: list[list[tuple[int, int, int]]],
                  to_change: tuple[int, int, int],
                  to_change_to: tuple[int, int, int]) -> list[list[tuple[int, int, int]]]:
    for column in image:
        for pixel in range(len(column)):
            if column[pixel] == to_change:  # Sustituye el pixel si coincide con el color a cambiar
                column[pixel] = to_change_to
    return image


def rotate_right(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    rotated_image = []
    for row in zip(*image):  # Recorre la imagen transpuesta
        rotated_image.append(list(reversed(row)))  # Invierte cada fila
    return rotated_image


def mirror(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    image_mirror = []
    for pixel in image[::-1]:  # Recorre la imagen desde el final al inicio para darle la vuelta
        image_mirror.append(pixel)
    return image_mirror


def rotate_colors(image: list[list[tuple[int, int, int]]], increment: int) -> list[list[tuple[int, int, int]]]:
    image_rotated = []
    for column in image:
        new_column = []
        for pixel in column:  # Se incrementa el color de cada color de cada pixel sin que pase de 255
            new_r = (pixel[0] + increment) % 256
            new_g = (pixel[1] + increment) % 256
            new_b = (pixel[2] + increment) % 256
            new_column.append((new_r, new_g, new_b))
        image_rotated.append(new_column)
    return image_rotated


def grayscale(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    image_grayscale = []
    for column in image:
        new_column = []
        for pixel in column:
            media = int(sum(pixel) / 3)  # Se calcula la media de los colores del pixel para pasarlo a escala de grises
            new_column.append((media, media, media))
        image_grayscale.append(new_column)
    return image_grayscale


def filter(image: list[list[tuple[int, int, int]]], r: float, g: float, b: float) -> list[list[tuple[int, int, int]]]:
    image_filter = []
    for column in image:
        new_column = []
        for pixel in column:
            new_r = min(int(pixel[0] * r), 255)
            new_g = min(int(pixel[1] * g), 255)
            new_b = min(int(pixel[2] * b), 255)
            new_column.append((new_r, new_g, new_b))
        image_filter.append(new_column)
    return image_filter


def blur(image: list[list[tuple[int, int, int]]]) -> list[list[tuple[int, int, int]]]:
    ...


def shift():
    ...


def crop():
    ...


