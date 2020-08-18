
'''''''&&&&&ITERATORS&&&&&&&&&'''''

'''''''class powtwo:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 3 ** self.n
            self.n += 1
            print(result)
        else:
            raise StopIteration


a = powtwo(3)
a.__iter__()

a.__next__()
a.__next__()
a.__next__()''''''''

''''''class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for i in myiter:
    print(i)''''''

''''GENERATORS'''''''


'''def rev_str(mystring):
    length = len(mystring)
    for i in range(-1, -length-1, -1):
        yield mystring[i]


a = rev_str("hello")
for s in a:
    print(s, end="")'''


def powtwo1(max1=0):
    n = 0
    while n <= max1:
        yield n**2
        n += 1


a = powtwo1(7)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
