# type: ignore

"""CircuitPython Essentials NeoPixel example"""
import time
import board
import neopixel
import random

def shuffle(l):
    result = list(l)
    for i in range(len(result)):
        ni = random.randint(0, len(result) - 1)
        result[i], result[ni] = result[ni], result[i]

    return result


class NeoStrip:
    def __init__(self, data_pin, num_pixels):
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(
            data_pin,
            num_pixels,
            brightness=1,
            auto_write=False,
            pixel_order=(1, 0, 2, 3))

    def fill(self, color):
        self.pixels.fill(color)
        self.pixels.show()


class Pallet:
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

    def random(self):
        return random.choice(self.colours())

strips = [
    NeoStrip(data_pin=board.GP14, num_pixels=10),
    NeoStrip(data_pin=board.GP15, num_pixels=10),
]

pallet = Pallet()

while True:
    for s, c in zip(strips, shuffle(pallet.colours())):
        s.fill(c)
    time.sleep(1)
 