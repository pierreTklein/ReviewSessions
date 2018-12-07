# Design a Class which represents the Cell. It should have the following attributes:
#   generation: What generation cell this is
#   id: the id for a Cell (for tracking where a cell came from)
#   num_chromosomes: int
#   size: the size of the Cell
#   split(): returns a tuple of new Cells, depending on the type of Cell it is.
# Come up with the following subclasses, which overrides the implementation of split
#   Sperm:
#       num_chromosomes: 23
#       size: 50
#       split(): Should return self
#   Spermatocyte:
#       num_chromosomes: 46
#       size: 45
#       split(): Should return four new Sperm Cells
#   Skin Cell: regular split
#       num_chromosomes: 46
#       size: 30
#       split(): Should return two new Skin Cells


class Cell:
    def __init__(self, id, num_chromosomes, size, generation=0):
        self.generation = generation
        self.id = id
        self.num_chromosomes = num_chromosomes
        self.size = size

    def split(self):
        return (
            Cell(self.id, self.num_chromosomes,
                 self.size, self.generation + 1),
            Cell(self.id, self.num_chromosomes, self.size, self.generation + 1)
        )


class Sperm(Cell):
    def __init__(self, id, generation=0):
        super().__init__(id, 23, 50, generation)

    def split(self):
        return (self)

    def __str__(self):
        return "Sperm" + " " + str(self.id) + " " + str(self.generation)


class Spermatocyte(Cell):
    def __init__(self, id, generation=0):
        super().__init__(id, 23, 50, generation)

    def split(self):
        return (
            Sperm(self.id, self.generation + 1),
            Sperm(self.id, self.generation + 1),
            Sperm(self.id, self.generation + 1),
            Sperm(self.id, self.generation + 1)
        )

    def __str__(self):
        return "Spermatocyte" + " " + str(self.id) + " " + str(self.generation)


class Skin(Cell):
    def __init__(self, id, generation=0):
        super().__init__(id, 46, 30, generation)

    def split(self):
        return (
            Skin(self.id, self.generation + 1),
            Skin(self.id, self.generation + 1)
        )

    def __str__(self):
        return "Skin cell" + " " + str(self.id) + " " + str(self.generation)


skinCell = Skin('1')
spermatocyteCell = Spermatocyte('2')

for cell in skinCell.split():
    print(cell)

for cell in spermatocyteCell.split():
    print(cell)
