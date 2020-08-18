'''class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(self.n):
            self.sides.append(0)

    def input_sides(self):
        for i in range(self.n):
            self.sides[i] = float(input("Enter side" + str(i+1)+":"))

    def display_of_sides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c))**.5
        print('area is :', area)


ob = Triangle()
ob.input_sides()
ob.find_area()'''


class Animal:
    def __init__(self, animal):
        print(animal, "is an Animal")


class Mammal(Animal):
    def __init__(self, mammal):
        print(mammal, " is a warm-blooded animal")
        super().__init__(mammal)


class NonWingedMammal(Mammal):
    def __init__(self, nonWingedAnimal):
        print(nonWingedAnimal, "can not fly")
        super().__init__(nonWingedAnimal)


class NonMarineMammal(Mammal):
    def __init__(self, nonMarineMammal):
        print(nonMarineMammal, "can not swim")
        super().__init__(nonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self, dog):
        print(dog, "has four legs")
        super().__init__(dog)


do = Dog("petty")
