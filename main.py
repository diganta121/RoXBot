# Modules
import pygame
from time import sleep

from os import system, name
from api.keybinds import Chat

from screen.colors import Colors
from screen.metrics import Metrics

from api.windows import WindowManager
from screen.functions import clear, getInfo

from api.user import equipItem, leaveGame, resetChar
from api.movement import Move, RandomMove, MoveToPos, resetPosition

keywords = ("mvf","mvb","mvr","mvl","cr","cl","lu","ld","lr","ll")

# Template functions
def _clear():

    """Cross-platform method of clearing the terminal"""
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")
    else:
        raise SystemError("Unsupported operating system %" % name)
def _stop():
    Chat("bye, stopping..")
    resetChar()
    _clear()
    pygame.quit()
    exit()


# Initialization
HANDLER = WindowManager()

pygame.init()

# Create window
SCREEN = pygame.display.set_mode((640, 480))

METRICS = Metrics(SCREEN, Colors.BLACK)

# Focus on ROBLOX only
HANDLER.focusROBLOX()

resetChar()

# Proceed once reset is done
sleep(7)

# Begin master loop
while True:

    # Fetch screen size and mouse positions
    X, Y, W, H = getInfo()
    _X, _Y, _W, _H = getInfo()

    # Update every frame
    clear(SCREEN, Colors.WHITE)

    # Invert coordinates for use in different grid
    Y = H - Y

    # Display our X and Y
    METRICS.setPos((X, Y))

    METRICS.show()

    # Set the line points
    points = [
        [(0, _Y), (W, _Y), Colors.GREEN],
        [(X, 0), (X, H), Colors.RED]
    ]

    # Show the lines
    for point_pair in points:

        pygame.draw.lines(SCREEN, point_pair[2], True, (point_pair[0], point_pair[1]), 1)

    # Handle events
    for event in pygame.event.get():

        # Exit script
        if event.type == pygame.QUIT:
            _stop()

        # Move to position
        if event.type == pygame.MOUSEBUTTONUP:

            MoveToPos((X, Y))
            Chat("position re")

        # Keystrokes
        if event.type == pygame.KEYDOWN:
            # Leave game
            if event.unicode.upper() == "L":
                resetPosition()
                leaveGame()
                _stop()

    pygame.display.update()
