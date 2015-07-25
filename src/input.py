from abc import abstractstaticmethod, ABCMeta


class Input(object):
    __metaclass__ = ABCMeta

    @abstractstaticmethod
    def anyKey():
        """ Return true if any key is currently down, false otherwise."""
        return

    @abstractstaticmethod
    def anyKeyDown():
        """ Return true if a key was pressed this update, false otherwise. """
        return

if __name__ == "__main__":
    Controller.test()
