import math


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __iter__(self):
        return iter((self.x, self.y))

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)


class Segment:
    def __init__(self, first_point, last_point):
        self._first_point = first_point
        self._last_point = last_point

    def __add__(self, vec2):
        return Segment(self.first_point + vec2, self.last_point + vec2)

    def __iadd__(self, other):
        self.first_point += other
        self.last_point += other
        return self

    @property
    def first_point(self):
        return self._first_point

    @first_point.setter
    def first_point(self, value):
        self._first_point = value

    @property
    def last_point(self):
        return self._last_point

    @last_point.setter
    def last_point(self, value):
        self._last_point = value

    def length(self):
        return Segment.distance(self._first_point, self._last_point)

    @staticmethod
    def distance(a, b):
        x1, y1 = a
        x2, y2 = b
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Chain(Segment):
    def __init__(self, vertices):
        assert len(vertices) > 1, "len(vertices) should be > 1"
        super().__init__(vertices[0], vertices[-1])
        self._vertices = []
        self.vertices = vertices

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        assert len(vertices) > 1, "len(vertices) should be > 1"
        print("Setter!!!")
        self._vertices = []
        for i in vertices:
            self._vertices.append(i)

        self.first_point = vertices[0]
        self.last_point = vertices[-1]

    @Segment.first_point.setter
    def first_point(self, value):
        self._first_point = value
        self._vertices[0] = value

    @Segment.last_point.setter
    def last_point(self, value):
        self._last_point = value
        self._vertices[-1] = value

    def length(self):
        res = 0
        for i in range(1, len(self._vertices)):
            res += Segment.distance(self._vertices[i], self._vertices[i - 1])
        return res

    def insert(self, vertex, index):
        self._vertices.insert(index, vertex)
        self.vertices = self._vertices

    def remove(self, index):
        assert len(self._vertices) == 2, "Cannot remove vertex from Chain with 2 vertices"
        del self._vertices[index]
        self.vertices = self._vertices




c = Chain([Vec2(0, 0), Vec2(1, 1)])
print(c.first_point)
print(c.last_point)
c.last_point = Vec2(2, 2)
c.first_point = Vec2(1, 1)
print(c.vertices[1])
c.insert(Vec2(3, 3), 2)
c.remove(0)
print(c.last_point)
print(c.first_point)
print(c.length())
