from collider2d import Collider2D
from vector2 import Vector2


class RectCollider(Collider2D):
    def __init__(self, xBounds, yBounds, name="RectCollider"):
        xBounds.sort()
        yBounds.sort()

        self.bounds = [xBounds, yBounds]
        self.xBounds, self.yBounds = self.bounds
        self.xMin, self.xMax = xBounds
        self.yMin, self.yMax = yBounds
        self.corners = [Vector2(x, y) for x in xBounds for y in yBounds]
        self.center = Vector2(*[sum(bound)/2 for bound in self.bounds])

        super(RectCollider, self).__init__(name)

    def getCenter(self):
        return self.center

    def getBoundingRadius(self):
        return Vector2.distance(self.corners[0], self.center)

    def testPoint(self, point):
        return (
            point.x > self.xMin
            and point.x < self.xMax
            and point.y > self.yMin
            and point.y < self.yMax
        )


if __name__ == "__main__":
    print(RectCollider([0, 6], [5, 3]))
