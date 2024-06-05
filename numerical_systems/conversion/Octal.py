class Octal:

    @staticmethod
    def to_decimal_builtin(octal: str) -> int:
        return int(octal, 8)

    @staticmethod
    def to_decimal(octal_number):
        decimal_number = 0

        for i in range(len(octal_number)):
            digit = int(octal_number[len(octal_number) - 1 - i])
            decimal_number += digit * (8 ** i)

        return decimal_number
