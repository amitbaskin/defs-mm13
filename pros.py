class User:
    def __init__(self, name, prof):
        self.name, self.prof = name, prof


class Engineer(User):
    def __init__(self, name, prof):
        super().__init__(name, prof)


class Technician(User):
    def __init__(self, name):
        super().__init__(name, 'Technician')


class Barber(User):
    def __init__(self, name):
        super().__init__(name, 'Barber')


class Politician(User):
    def __init__(self, name):
        super().__init__(name, 'Politician')
    def study(self):
        return


class ElectricalEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, 'Electrical Engineer')


class ComputersEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, 'Computers Engineer')


class MachinesEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, 'Machines Engineer')


if __name__ == '__main__':
    base = None
    try:
        base = eval(input('Please enter name of base class (blank if none): '))
    except SyntaxError:
        base = object
    new_cls = type(input('Please enter the name of new class: '), (base,), {})
    setattr(new_cls, input(f'Please enter name of new method for class {new_cls.__name__}: '), lambda x: None)
    setattr(new_cls, input(f'Please enter name of new attribute for class {new_cls.__name__}: '), None)
    print(f'Class Student created with base class: {new_cls.__base__}')
    print(f'Class __name__ is: {new_cls.__name__}')
    print(f'Class __dict__ is: {new_cls.__dict__}')
