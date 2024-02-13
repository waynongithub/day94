import time
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from PIL import ImageGrab
# https://github.com/gauthsvenkat/pyKey


# showKeys()
def get_color_sum(px, minx, maxx, stepx, y):
    colorsum = 0
    i = 1
    for x in range(minx, maxx, stepx):
        i += 1
        color = px[x, y]
        colorsum += color[0]
    average = colorsum / i
    return average


while True:
    # detect cactus and low-flyind bird and JUMP
    minx, maxx, stepx, y = 720, 810, 1, 350
    px = ImageGrab.grab().load()
    avg = get_color_sum(px, minx, maxx, stepx, y)
    # print(f"avg={avg}")
    if avg < 240:
        # print(f"avg={avg}")
        pressKey('UP')
        releaseKey('UP')

    # detect high-flyind bird and DUCK
    px = ImageGrab.grab().load()
    maxx, y = 810, 326
    avg = get_color_sum(px, minx, maxx, stepx, y)
    # print(f"avg={avg}")
    if avg < 240:
        # print(f"avg={avg}")
        pressKey('DOWN')
        time.sleep(0.2)
        releaseKey('DOWN')

    # time.sleep(0.0001)


