'''class cel:
    def __init__(self, temp):
        self.temperature = temp

    def to_fahrenheit(self):
        return self.temperature * 1.2 + 32

    @property
    def temperature(self):
        print(" getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print(" setting value")
        if value < -273:
            raise ValueError("ooofff")
        self._temperature = value


human = cel(37)
print(human.temperature)'''


class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        # self.gotmarks = self.name + ' obtained ' + self.mark + ' marks'

    @property
    def gotmarks(self):
        print("getting value...")
        return self.name + ' obtained ' + self.mark + ' marks'

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, *rand, mark = sentence.split(' ')
        self.name = name
        self.mark = mark


st = Student("jacki", "25")
print(st.gotmarks)
st.gotmarks = "ali  easily high foc fight 34"
print(st.gotmarks)


'''class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineappple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineappple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        password = input("enter pass : ")
        if password == "pook":
            self._pineappple_allowed = value
        else:
            raise ValueError(" you are not allowed to get access")


pizza = Pizza(["corn", "potato"])
print(pizza._pineappple_allowed)
pizza.pineapple_allowed = "gamma"
print(pizza.pineapple_allowed)'''