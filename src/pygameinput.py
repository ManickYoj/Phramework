from input import Input
import pygame
import sys
from vector2 import Vector2

PYGAME_KEY_MAP = {

}

PYGAME_MOUSE_BUTTON_MAP = {
    "LEFT": 1,
    "MIDDLE": 3,
    "RIGHT": 2,
}


class PygameInput(Input):
    # ----- Meta Methods ----- #
    def __init__(self):
        self._clearVariables()
        self.EVENT_MAP = {
            "KEYDOWN": lambda self, *args: self._keysDown.append(args[1]),
            "KEYUP": lambda self, *args: self._keysUp.append(args[0]),
            "MOUSEMOTION": lambda *args: None,
            "MOUSEBUTTONDOWN":
                lambda self, *args: self._mouseButtonsDown.append(args[1]),
            "MOUSEBUTTONUP":
                lambda self, *args: self._mouseButtonsUp.append(args[1]),
            "QUIT": lambda *args: sys.exit(0)
        }

    def _clearVariables(self):
        self._keys = pygame.key.get_pressed()
        self._keysDown = []
        self._keysUp = []
        self._mouseButtons = []
        self._mouseButtonsDown = []
        self._mouseButtonsDown = []
        self._mouseDelta = Vector2(0, 0)

    def flushInput(self, time, deltaTime):
        """ Drop input events and set up next frame. """
        self._clearVariables()
        self._mouseDelta = Vector2(*pygame.mouse.get_rel())
        for index, state in enumerate(pygame.mouse.get_pressed()):
            if state:
                self._mouseButtons.append(index)

        while True:
            event = pygame.event.get()
            try:
                self.EVENT_MAP[event.type]()
            except KeyError:
                print("Unhandled pygame event: {}".format(event.type))

    # ----- Key Input ----- #
    def anyKey(self):
        """ Boolean: is any key held down? """
        return bool(self._keys)

    def anyKeyDown(self):
        """ Boolean: was any key pressed this frame? """
        return bool(self._keysDown)

    def anyKeyUp(self):
        """ Boolean: was any key released this frame? """
        return bool(self._keysUp)

    def getKey(self, keyName):
        """ Boolean: is the given key held down? """
        return PYGAME_KEY_MAP[keyName] in self._keys

    def getKeyDown(self, keyName):
        """ Boolean: was the given key pressed this frame? """
        return PYGAME_KEY_MAP[keyName] in self._keysDown

    def getKeyUp(self, keyName):
        """ Boolean: was the given key released this frame? """
        return PYGAME_KEY_MAP[keyName] in self._keysUp

    # ----- Mouse Input ----- #
    def _convertButtonName(self, buttonName):
        try:
            buttonName = buttonName.upper()
            return PYGAME_MOUSE_BUTTON_MAP[buttonName]

        # If the buttonName is not a string
        except AttributeError:
            return buttonName

        # If the buttonName is not in the button mapping
        except KeyError:
            raise ValueError("Mouse button name was invalid.")

    def getMouseButton(self, buttonNumberOrName):
        """ Boolean: is the given mouse button held down? """
        buttonNumber = self._convertButtonName(buttonNumberOrName)
        return buttonNumber in self._mouseButtons

    def getMouseDown(self, buttonNumberOrName):
        """ Boolean: was the given mouse button clicked this frame? """
        buttonNumber = self._convertButtonName(buttonNumberOrName)
        return buttonNumber in self._mouseButtonsDown

    def getMouseUp(self, buttonNumberOrName):
        """ Boolean: was the given mouse button released this frame? """
        buttonNumber = self._convertButtonName(buttonNumberOrName)
        return buttonNumber in self._mouseButtonsUp

    def getMousePos(self):
        """ Vector2: x, y position of the mouse. """
        return Vector2(*pygame.mouse.get_pos())

    def getMouseDelta(self):
        """ Vector2: dx, dy of mouse since last frame. """
        return self._mouseDelta
