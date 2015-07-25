from Component import Component


class Transform (Component):
    def __init__(self,
                 position=(0, 0, 0),
                 rotation=(0, 0, 0),
                 scale=(0, 0, 0),
                 *args,
                 **kwargs):

        super(Transform, self).__init__("Transform", *args, **kwargs)

        self.position = position
        self.rotation = rotation
        self.scale = scale
