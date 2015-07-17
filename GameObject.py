from abc import ABCMeta


class GameObject (object):
    __metaclass__ = ABCMeta

    _registry = {}

    @staticmethod
    def get(_id):
        if _id in GameObject._registry:
            return GameObject._registry[id]

    @staticmethod
    def updateAll(t, dt):
        for obj in GameObject._registry.values():
            obj.update(t, dt)

    def __init__(self, name="GameObject", components=[], *args, **kwargs):
        self.name = name
        self.components = []
        self.addComponents(components)

        # Register Object
        GameObject._registry[id(self)] = self

    def parentTo(self, parent):
        """ GameObj wrapper for transform's parent method. """
        self.transform.parentTo(parent)

    def addCompontent(self, component):
        component.claim(self)
        self.components.append(self)

        component.checkDependencies()
        component.awake()

    def addComponents(self, components):
        for component in components:
            component.claim(self)
            self.components.append(component)

        for component in self.components:
            component.checkDependencies()
            component.awake()

    def getComponent(self, componentType):
        for component in self.components:
            if isinstance(component, componentType):
                return component

    def update(self, t, dt):
        for component in self.components:
            component.update(t, dt)

    def __str__(self):
        return "{} (id: {})".format(self.name, id(self))


if __name__ == "__main__":
    from Transform import Transform
    g = GameObject(components=[Transform()])
    print(g.getComponent(Transform))
