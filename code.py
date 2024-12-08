# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# type: ignore

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.DATA
num_pixels = 50

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


class pallet:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)

    def colours(self):
        return [
            self.RED,
            self.YELLOW,
            self.GREEN,
            self.CYAN,
            self.BLUE,
            self.PURPLE,
        ]

def flash_colours(pixels, RED, GREEN, BLUE):
    pixels.fill(RED)
    pixels.show()
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

def chase_colours(color_chase, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE):
    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

while True:
    flash_colours(pixels, pallet.RED, pallet.GREEN, pallet.BLUE)

    chase_colours(color_chase, pallet.RED, pallet.YELLOW, pallet.GREEN, pallet.CYAN, pallet.BLUE, pallet.PURPLE)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
 