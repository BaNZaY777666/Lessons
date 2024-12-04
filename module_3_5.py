def get_multiplied_digits(number):
    str_numbers = str(number)
    str_numbers = str_numbers.replace('0','')
    if len(str_numbers) > 1:
        first = int(str_numbers[0])
        return first * get_multiplied_digits(int(str_numbers[1:]))
    else:
        return int(str_numbers)


result_1 = get_multiplied_digits(402030)
print(result_1)
result_2 = get_multiplied_digits(402030)
print(result_2)