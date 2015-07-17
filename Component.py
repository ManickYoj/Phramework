from Exceptions import DependencyException


class Component (object):
    """ Superclass for all component objects. """

    def __init__(self, name, owner=None, dependencies=[]):
        self.name = name
        self.owner = owner
        self.dependencies = dependencies

    def checkDependencies(self):
        for dependencyType in self.dependencies:
            if not(self.owner and self.owner.getComponent(dependencyType)):
                raise DependencyException(
                    "Component {} is dependent upon a {} component, "
                    "and that dependency is unfufilled."
                    .format(
                        self.gameObject() or "unowned " + self.name,
                        dependencyType.__name__
                    )
                )

    def claim(self, owner):
        self.owner = owner

    def gameObject(self):
        return self.owner

    def awake(self):
        pass

    def update(self, t, dt):
        pass

    def __str__(self):
        if not self.owner:
            return "Unowned {}".format(self.name)
        return self.name + " of " + str(self.owner)
