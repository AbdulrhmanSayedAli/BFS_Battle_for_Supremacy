import sys
import os

WIDTH, HEIGHT = 1200, 700
FRAME_RATE_PER_SECOND = 30
DIALOG_WIDTH, DIALOG_HEIGHT = (400, 300)


if getattr(sys, "frozen", False):
    # Running as an executable
    ASSETS_PATH = "_internal/assets"
else:
    # running as script
    ASSETS_PATH = "assets"

IMAGES_PATH = os.path.join(ASSETS_PATH, "images")
BOARD_SIZE = (10, 10)
BOARD_SIZE_WIDTH = BOARD_SIZE[0]
BOARD_SIZE_HEIGHT = BOARD_SIZE[1]
ROCK_NUM = 20
