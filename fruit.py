class AppleBasket:

    def __init__(self, apple_color, apple_quantity):
        self.apple_color, self.apple_quantity = apple_color, apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return f'A basket of {self.apple_quantity} {self.apple_color} apple{"s" if self.apple_quantity != 1 else ""}.'


if __name__ == '__main__':
    print('Example1: ', AppleBasket('red', 4), '\n', 'Example2: ', AppleBasket('blue', 50), sep='')
