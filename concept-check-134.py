def sum_digits(two_digit_number):
    ones = two_digit_number % 10
    tens = two_digit_number // 10
    total = ones + tens
    return total