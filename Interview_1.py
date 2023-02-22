def add_digits(number):
    num = 0
    while number/10 != 0:
        num += number%10
        number = number/10
    num += number
    if num / 10 != 0:
        return add_digits(num)
    return num

def main():
    print(add_digits(74))

if __name__ == '__main__':
    main()