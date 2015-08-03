from vector2 import Vector2


class Ray2D(object):
    def __init__(self, origin):
        self.origin = Vector2(*origin)

    def getOrigin(self):
        return self.origin
