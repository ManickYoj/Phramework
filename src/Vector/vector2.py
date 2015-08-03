from vector import Vector


class Vector2(Vector):
    @staticmethod
    def identity():
        return Vector2(0, 0)

    @staticmethod
    def up():
        return Vector2(0, 1)

    @staticmethod
    def down():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(1, 0)

    @staticmethod
    def left():
        return Vector2(-1, 0)

    def __init__(self, u, v):
        super(Vector2, self).__init__(u, v)
        self.x = self.value[0]
        self.y = self.value[1]

if __name__ == "__main__":
    print(Vector2(0, 2))
