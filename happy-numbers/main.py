seen_numbers = {}


def add_to_seen_numbers(number, calculated_sums, is_happy_number):
    seen_numbers[number] = is_happy_number
    for number in calculated_sums:
        seen_numbers[number] = is_happy_number


def calculate_digit_square_sum(number):
    number_str = str(number)
    digit_square_sum = 0

    for digit_str in number_str:
        digit = int(digit_str)
        digit_square_sum += digit**2

    return digit_square_sum


def is_happy_number(number):
    number_copy = number
    calculated_sums = set()

    while True:
        digit_square_sum = calculate_digit_square_sum(number_copy)

        if digit_square_sum in calculated_sums:
            return False
        else:
            calculated_sums.add(digit_square_sum)

        if digit_square_sum in seen_numbers.keys():
            return seen_numbers[digit_square_sum]

        if digit_square_sum == 1:
            add_to_seen_numbers(number, calculated_sums, True)
            return True
        else:
            number_copy = digit_square_sum
            continue


a, b = map(int, input().split())

happy_numbers = []

for number in range(a, b + 1):
    flag = is_happy_number(number)

    if flag is True:
        happy_numbers.append(number)

print(len(happy_numbers))
