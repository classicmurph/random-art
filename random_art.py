import random

from math import sin, cos, tan, tanh, pi, sinh, cosh

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

funx = ['sin(x)', 'cos(y)', '(2 * sin(x))', '2 * y',
        'sinh(x)', 'cos(x)', 'tan(y)']


class Expression:
    def __init__(self):
        self.commands = []


    def evaluate(self, x, y):
        value = '1'
        for (command, coord) in self.commands:
            if command == "norm" and coord == "x":
                for _ in range(random.randint(1, 5)):
                    value = value + ' * ' + random.choice(funx)
            elif command == "norm" and coord == "y":
                for _ in range(random.randint(1, 5)):
                    value = value + ' * ' + random.choice(funx)
            elif command == "crazy" and coord == "x":
                for _ in range(random.randint(3, 12)):
                    value = value + ' * ' + random.choice(funx)
            else:
                for _ in range(random.randint(3, 12)):
                    value = value + ' * ' + random.choice(funx)


        return eval(value)


    def __str__(self):
        return str(self.commands)



def avg(a, b):
    return (a + b) / 2



def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    expr = Expression()

    for _ in range(3):
        if random.random() > 0.5:
            x_or_y = "x"
        else:
            x_or_y = "y"

        if random.random() > 0.5:
            norm_or_crazy = "norm"
        else:
            norm_or_crazy = "crazy"

        expr.commands.append([norm_or_crazy, x_or_y])

    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
