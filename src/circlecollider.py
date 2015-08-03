from collider2d import Collider2D
from vector2 import Vector2


class CircleCollider(Collider2D):
    def __init__(self, center, radius, name="CircleCollider"):
        self._radius = radius
        self._center = Vector2(*center)
        super(CircleCollider, self).__init__(name)

    def getCenter(self):
        return self._center

    def getBoundingRadius(self):
        return self._radius

    def testPoint(self, point):
        return Vector2.distance(point, self._center) < self._radius

if __name__ == "__main__":
    print(CircleCollider((0, 6), 4).getCenter())
