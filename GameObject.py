from abc import ABCMeta


class GameObject (object):
    __metaclass__ = ABCMeta

    _registry = {}

    @staticmethod
    def get(name):
        if name in GameObject._registry:
            return GameObject._registry[name]

    @staticmethod
    def updateAll(t, dt):
        for obj in GameObject._registry.values():
            obj.update(t, dt)

    def __init__(self, name, pos, depth=0, components=[]):
        self.name = name
        self.components = []
        self.addComponents(components)

        # Register Object
        GameObject._registry[name] = self

    def parentTo(self, parent):
        """ GameObj wrapper for transform's parent method. """
        self.transform.parentTo(parent)

    def addComponent(self, component):
        component.claim(self)
        self.components.append(component)
        component.awake()

    def addComponents(self, components):
        for component in components:
            self.addComponent(component)

    def getComponent(self, componentType):
        for component in self.components:
            if isinstance(component, componentType):
                return component

    def update(self, t, dt):
        for component in self.components:
            component.update(t, dt)

    def __str__(self):
        return self.name
