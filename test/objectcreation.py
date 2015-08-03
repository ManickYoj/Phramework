from gameobject import GameObject
from transform import Transform
from camera import Camera


if __name__ == "__main__":
    g = GameObject(
        name="Main Camera",
        components=[
            Transform(),
            Camera(),
        ],
    )

    print(g)
    print(g.getComponent(Transform))
    print(g.getComponent(Camera))
