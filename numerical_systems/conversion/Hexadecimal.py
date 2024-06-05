class Hexadecimal:

    @staticmethod
    def to_decimal_builtin(hexadecimal: str) -> int:
        return int(hexadecimal, 16)

    @staticmethod
    def to_decimal(hexadecimal):
        decimal = 0
        hexadecimal_digits = "0123456789ABCDEF"

        for i in range(len(hexadecimal)):
            digit = hexadecimal[len(hexadecimal) - 1 - i].upper()
            value = hexadecimal_digits.index(digit)
            decimal += value * (16 ** i)

        return decimal
