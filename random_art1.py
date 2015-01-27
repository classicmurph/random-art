import random

from math import sin, cos, tan, tanh, pi, sinh, cosh

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

class Expression:
    def __init__(self):
        self.commands = []

    def evaluate(self, x, y):
        value = 1
        for (command, coord) in self.commands:
            if command == "sin" and coord == "x":
                value *= sin(tanh(pi * avg(x, avg(y, tanh(x**2)))))
            elif command == "sin" and coord == "y":
                value *= cos(tan((pi * avg(y, avg(x,tan(y**2))))))
            elif command == "cos" and coord == "x":
                value *= cos(tan(pi * avg(x, avg(y, tan(x**2)))))
            elif command == "cos" and coord == "y":
                value *= sin(tanh(pi * avg(y, avg(x, tanh(y**2)))))

        return value

    def __str__(self):
        return str(self.commands)



def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    x = random.randint(1, 10000)
    y = random.randint(1, 10000)

    # expr = Expression()

    expr = '(x*y)'

    funx = ['sin(x/2)', 'cos(y ** 3)', '(2 * sin(x))', 'y**6', '(x)',
            'tan(x ** random.randint(0, 40))', 'cos(y*x**2)', '100',
            'random.randrange(0, 100000)*cos(y)']

    for _ in range(random.randint(10, 40)):
        expr = expr + ' * ' + random.choice(funx)

    return expr



def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return eval(expr)
