class Figure:
    def P(self):
        raise Exception('Error')

    def S(self):
        raise Exception('Error')


class Triangle(Figure):
    def __init__(self, sides):
        self.sides = sides

    def P(self):
        p = sum(self.sides)
        return p

    def S(self):
        p = self.P() / 2
        s = (p(p-self.sides[0])(p-self.sides[1])(p-self.sides[3]))**(1/2)
        return s


t = Triangle([3, 4, 5])
print(t.P(), t.S())


class Rectangle(Figure):
    def __init__(self, sides):
        self.a = sides[0]
        self.b = sides[1]

    def P(self):
        p = (self.a + self.b) * 2
        return p

    def S(self):
        s = self.a * self.b
        return s


r = Rectangle([3, 4])
print(r.P(), t.S())

'''
    def S(self):
        p2 = self.P()/2
        s = pow(p*(p-)



'''
