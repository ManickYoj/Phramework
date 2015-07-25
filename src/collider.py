from __future__ import division
import kdtree
from component import Component
from transform import Transform
from vector import Vector
from abc import ABCMeta, abstractmethod


class Collider2D(Component):
    __metaclass__ = ABCMeta

    _quadTree = kdtree.create(dimensions=2)
    _rMax = None

    @staticmethod
    def register(newCollider):
        br = newCollider.getBoundingRadius()
        if not Collider2D._rMax or br > Collider2D._rMax:
            Collider2D._rMax = br

        Collider2D._quadTree.add(newCollider)

    def __init__(self, name="Collider2D"):
        Collider2D.register(self)
        super(Collider2D, self).__init__(name,
                                         dependencies=[Transform])

    def __getitem__(self, key):
        return self.getCenter()[key]

    def __len__(self):
        return len(self.getCenter())

    @abstractmethod
    def getCenter(self):
        return

    @abstractmethod
    def getBoundingRadius(self):
        return


class RectCollider(Collider2D):
    def __init__(self, xBounds, yBounds, name="RectCollider"):
        self.bounds = [xBounds, yBounds]

        self.corners = [Vector(x, y) for x in xBounds for y in yBounds]

        self.center = Vector(*[sum(bound)/2 for bound in self.bounds])
        super(RectCollider, self).__init__(name)

    def getCenter(self):
        return self.center

    def getBoundingRadius(self):
        return Vector.distance(self.corners[0], self.center)

if __name__ == "__main__":
    print(RectCollider([0, 6], [5, 3]))
