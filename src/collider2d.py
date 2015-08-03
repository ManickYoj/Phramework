from __future__ import division
import kdtree
from component import Component
from transform import Transform
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

    @staticmethod
    def raycast(ray2d):
        considered = Collider2D._quadTree.search_nn_dist(ray2d.getOrigin(),
                                                         Collider2D._rMax)

        hits = []

        for collider in considered:
            if collider.testPoint(ray2d.getOrigin()):
                hits.append(collider)

        return hits

    def __init__(self, name="Collider2D"):
        Collider2D.register(self)
        super(Collider2D, self).__init__(name,
                                         dependencies=[Transform])

    def __getitem__(self, key):
        return self.getCenter()[key]

    def __len__(self):
        return len(self.getCenter())

    @abstractmethod
    def testPoint(self, point):
        return

    @abstractmethod
    def getCenter(self):
        return

    @abstractmethod
    def getBoundingRadius(self):
        return
