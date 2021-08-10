if __name__ == '__main__':
    Rainful_mi = "45, 65, 70.4, 82.6, 20.1, 90.8, 76.1, 30.92, 46.8, 67.1, 79.9"
    num_rainy_months = sum(float(num) > 75 for num in Rainful_mi.split(', '))
