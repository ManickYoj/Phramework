from __future__ import division
import operator
from numbers import Number


class Vector (object):
    @staticmethod
    def magnitude(vec):
        return sum([x**2 for x in vec]) ** .5

    @staticmethod
    def distance(vec1, vec2):
        difference = vec1 - vec2
        return Vector.magnitude(difference)

    def __init__(self, *args):
        self.value = args

    def __add__(self, vector):
        return self._tryOperation(vector, operator.add, "to add")

    def __radd__(self, vector):
        return self + vector

    def __sub__(self, vector):
        return self._tryOperation(vector, operator.sub, "to subtract with")

    def __mul__(self, scalarOrVector):
        if isinstance(scalarOrVector, Vector):
            return self._tryOperation(scalarOrVector,
                                      operator.mul,
                                      "elementwise multiplication of")
        elif isinstance(scalarOrVector, Number):
            return Vector(*[elem * scalarOrVector for elem in self.value])
        else:
            msg = ("Attempted vector multiplication with a "
                   "parameter that was neither a scalar nor Vector.")
            raise TypeError(msg)

    def __rmul__(self, scalarOrVector):
        return self * scalarOrVector

    def __truediv__(self, scalarOrVector):
        if isinstance(scalarOrVector, Vector):
            return self._tryOperation(scalarOrVector,
                                      operator.truediv,
                                      "elementwise division of")
        elif isinstance(scalarOrVector, Number):
            return Vector(*[elem / scalarOrVector for elem in self.value])
        else:
            msg = ("Attempted vector multiplication with a "
                   "parameter that was neither a scalar nor Vector.")
            raise TypeError(msg)

    def __str__(self):
        return str(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __len__(self):
        return len(self.value)

    def _tryOperation(self, vector, operation, operationName):
        """
        Private helper method to shorthand trying an arithmetic operation.
        """
        try:
            return Vector(*map(operation, self.value, vector.value))
        except TypeError:
            msg = 'Attempted {} vectors of \
                   unequal length'.format(operationName)

            raise ArithmeticError(msg)

# ----- Unit Tests ----- #
if __name__ == "__main__":
    vec1 = Vector(1, 2, 3)
    vec2 = Vector(3, 2, 1)
    vec3 = Vector(3, 5, 2)
    shortVec = Vector(2, 3)
    longVec = Vector(4, 2, 3, 5)

    # Test addition
    print("Sum: " + str(vec1 + vec2 + vec3))

    # Test subtraction
    print("Difference: " + str(vec3 - vec2))

    # Test scalar multiplication
    print("Scalar Product: " + str(5 * vec1 * 5))

    # Test element-wise multiplication
    print("Vector Product: " + str(vec1 * vec2))

    # Test scalar division
    print(vec1 / 5)

    # Test element-wise division
    print("Vector Quotient: " + str(vec1 / vec2))
