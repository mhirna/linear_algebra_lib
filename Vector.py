class Vector:
    def __init__(self, coords):
        try:
            if not coords:
                raise ValueError
            self.dimension = len(coords)
            self.coordinates = tuple(coords)

        except ValueError:
            raise ValueError("Coordinates must be not empty")

        except TypeError:
            raise TypeError("Coordinates should be iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector should be added to another vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors should have same dimensions")
        coordinates = [self.coordinates[i] + other.coordinates[i] for i in range(self.dimension)]
        return Vector(coordinates)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Vector should be added to another vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors should have same dimensions")
        coordinates = [self.coordinates[i] - other.coordinates[i] for i in range(self.dimension)]
        return Vector(coordinates)

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            return Vector([other * i for i in self.coordinates])
        #TODO mult by vector

    def get_magnitude(self):
        return sum([i**2 for i in self.coordinates]) ** 0.5

    def normalize(self):
        try:
            magnitude = self.get_magnitude()
            return Vector([i / magnitude for i in self.coordinates])

        except ZeroDivisionError:
            raise ZeroDivisionError("Zero vector can not be normalized")
