from Component import Component


class Transform (Component):
    def __init__(self, *args, **kwargs):
        super(Transform, self).__init__("Transform", *args, **kwargs)
