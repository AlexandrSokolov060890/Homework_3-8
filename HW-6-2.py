class Road:
    def __init__(self, _length, _width):
        self._lenght = _length
        self._width = _width

    def square(self):
        return self._lenght * self._width


class Volume:
    def __init__(self, _mass, _depth):
        self._mass = _mass
        self._depth = _depth

    def volume(self):
        return self._mass * self._depth


r = Road(20, 5000)
v = Volume(25, 5)
print(r.square() * v.volume())
