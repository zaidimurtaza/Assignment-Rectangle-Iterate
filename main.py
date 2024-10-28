class Rectangle:
    def __init__(self, length: int , width: int ):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# test
rect = Rectangle(10, 5)

# Iterating over the Rectangle
for dimension in rect:
    print(dimension)
