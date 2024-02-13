import time
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from PIL import ImageGrab
# https://github.com/gauthsvenkat/pyKey
# check mouse coordinates:
# $ while true; do clear; xdotool getmouselocation; sleep 0.1; done;

# showKeys()
def any_dark_pixel(px, minx, maxx, stepx, y):
    for x in range(minx, maxx, stepx):
        color = px[x, y]
        print(f"{color[0]}, maxx={maxx}")
        if color[0] < 200:
            print(f"------{color[0]}")
            return True
    return False

# actions = []
while True:
    # # detect cactus and low-flyind bird and JUMP
    minx, maxx, stepx, y = 750, 820, 1, 350
    px = ImageGrab.grab().load()
    if any_dark_pixel(px, minx, maxx, stepx, y):
        pressKey('UP')
        releaseKey('UP')

    # # detect high-flyind bird and DUCK
    py = ImageGrab.grab().load()
    maxx, y = 810, 314
    if any_dark_pixel(py, minx, maxx, stepx, y):
        pressKey('DOWN')
        print(f"----------->DUCK")
        time.sleep(0.2)
        releaseKey('DOWN')



