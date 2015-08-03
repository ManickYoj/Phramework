from abc import ABCMeta, abstractmethod

# TODO: Implement virtual buttons and axes


class Input(object):
    __metaclass__ = ABCMeta

    # ----- Meta Methods ----- #
    @abstractmethod
    def flushInput(time, deltaTime):
        """ Drop input events and set up next frame. """
        return

    # ----- Key Input ----- #
    @abstractmethod
    def anyKey():
        """ Boolean: is any key held down? """
        return

    @abstractmethod
    def anyKeyDown():
        """ Boolean: was any key pressed this frame? """
        return

    @abstractmethod
    def anyKeyUp():
        """ Boolean: was any key released this frame? """
        return

    @abstractmethod
    def getKey(keyName):
        """ Boolean: is the given key held down? """
        return

    @abstractmethod
    def getKeyDown(keyName):
        """ Boolean: was the given key pressed this frame? """
        return

    @abstractmethod
    def getKeyUp(keyName):
        """ Boolean: was the given key released this frame? """
        return

    # ----- Mouse Input ----- #
    @abstractmethod
    def getMouseButton(buttonNumberOrName):
        """ Boolean: is the given mouse button held down? """
        return

    @abstractmethod
    def getMouseDown(buttonNumberOrName):
        """ Boolean: was the given mouse button clicked this frame? """
        return

    @abstractmethod
    def getMouseUp(buttonNumberOrName):
        """ Boolean: was the given mouse button released this frame? """
        return

    @abstractmethod
    def getMousePos():
        """ Vector2: x, y position of the mouse. """
        return

    @abstractmethod
    def getMouseDelta():
        """ Vector2: dx, dy of mouse since last frame. """
        return
