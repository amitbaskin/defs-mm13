import importlib
import inspect
import sys

import fruit


def deco(f, code):
    def ret(*args):
        eval(code)
        return f(*args)
    return ret


def affect(module, code):
    for cls in inspect.getmembers(sys.modules[module.__name__], inspect.isclass):
        for attr, item in cls[1].__dict__.items():
            if callable(item):
                if attr == '__init__':
                    continue
                setattr(cls[1], attr, deco(item, code))


if __name__ == "__main__":
    affect(importlib.import_module(input('Enter python file name: ').rstrip('.py')), 'print("Added code!")')
    basket1 = fruit.AppleBasket('red', 4)
    basket2 = fruit.AppleBasket('blue', 50)
    print(basket1)
    basket1.increase()
    print(basket2)
    basket2.increase()





