from Component import Component
from Transform import Transform


class Camera (Component):
    _active = None

    def __init__(self, active=False, *args, **kwargs):
        if active or not Camera._active:
            Camera._active = self

        super(Camera, self).__init__(
            name="Camera",
            dependencies=[Transform],
            *args,
            **kwargs)

# Tests
if __name__ == "__main__":
    Camera()
    print(Camera._active)
