class C:
    def __init__(self):
        self._x = "property test"

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


c = C()
print(c.x)