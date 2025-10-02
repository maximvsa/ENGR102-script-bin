num = int(input('Enter a 4-digit number: '))

num1 = num // 1000
num2 = (num % 1000) // 100
num3 = ((num % 1000) % 100) // 10
num4 = (((num % 1000) % 100) % 10)

if (num1 ** num1 + num2 ** num2 + num3 ** num3 + num4 ** num4 == num):
    print(f'{num} is a Munchausen number.')
else:
    print(f'{num} is not a Munchausen number.')