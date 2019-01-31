import numpy as np
from collections import defaultdict


class Cart:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.intersection = 0
        self.dead = False


def turn_cart(cart, part):
    if not part:
        return
    if part == "\\":
        if cart.direction.real == 0:
            cart.direction *= -1j
        else:
            cart.direction *= +1j
    if part == "/":
        if cart.direction.real == 0:
            cart.direction *= +1j
        else:
            cart.direction *= -1j
    if part == "+":
        cart.direction *= -1j * +1j ** cart.intersection
        cart.intersection = (cart.intersection + 1) % 3


with open('./input/day13.txt', 'r') as lines:
    lines = [list(line) for line in lines.read().split('\n')]
    tracks = defaultdict(lambda: "")
    carts = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "\n":
                continue
            if char in "^v<>":
                direction = {
                    "^": -1j,
                    "v": +1j,
                    "<": -1,
                    ">": +1
                }[char]
                carts.append(Cart(x + y * 1j, direction))
                part = {
                    "^": "|",
                    "v": "|",
                    "<": "-",
                    ">": "-"
                }[char]
            else:
                part = char
            if part in "\\/+":
                tracks[(x + y * 1j)] = part

    # while True:
    #     carts.sort(key=lambda c: (c.position.imag, c.position.real))
    #     for ci, cart in enumerate(carts):
    #         cart.position += cart.direction
    #         if any(c2.position == cart.position for c2i, c2 in enumerate(carts) if c2i != ci):
    #             print(str(int(cart.position.real)) + "," + str(int(cart.position.imag)))
    #             break
    #         part = tracks[cart.position]
    #         turn_cart(cart, part)
    #     else:
    #         continue
    #     break

    while len(carts) > 1:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            if cart.dead:
                continue
            cart.position += cart.direction
            for ci2, cart2 in enumerate(carts):
                if ci != ci2 and cart.position == cart2.position and not cart2.dead:
                    cart.dead = True
                    cart2.dead = True
                    break
            if cart.dead:
                continue
            part = tracks[cart.position]
            turn_cart(cart, part)
        carts = [c for c in carts if not c.dead]
    if not carts:
        print("ERROR: there's an even number of carts, there's isn't one cart left at the end")
    cart = carts[0]

    print(str(int(cart.position.real)) + "," + str(int(cart.position.imag)))