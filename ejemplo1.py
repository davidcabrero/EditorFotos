#!/usr/bin/env python

from images import read_img, write_img

# Each list in this list is a column of pixels (x is the index of that list)
# Each eleement in that list is a pixel (y is the index within that list)
pixels = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
          [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
          [(255, 255, 0), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255)],
          [(255, 255, 0), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255)],
          [(255, 255, 0), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255)],
          [(255, 255, 0), (255, 255, 255), (255, 255, 255), (0, 0, 255), (255, 255, 255)]]

write_img(pixels, 'bands.png')
pixels = read_img('bands.png')
write_img(pixels, 'bands2.jpg')
write_img(pixels, 'bands2.png')
