class Decimal:
    """
    Convert decimal to binary, octal and hexadecimal.
    """

    @staticmethod
    def to_binary(decimal: int) -> str:
        if decimal > 0:
            binary_digits = []
            number = abs(decimal)
            while number > 0:
                binary_digits.insert(0, str(number % 2))
                number //= 2
            return ''.join(binary_digits)

        elif decimal == 0:
            return '0'

    @staticmethod
    def to_binary_builtin(decimal: int) -> str:
        """
        Convert to binary using the built-in bin() function.
        """
        return bin(decimal)

    @staticmethod
    def to_octal(decimal: int):
        """
        Convert to octal.
        """
        if decimal > 0:
            octal_digits = []
            while decimal > 0:
                octal_digits.insert(0, str(decimal % 8))
                decimal = decimal // 8
            return int(''.join(octal_digits))

        elif decimal == 0:
            return '0'

    @staticmethod
    def to_octal_builtin(decimal: int) -> int:
        """
        Convert to octal using the built-in oct() function.
        """
        return int(oct(abs(decimal))[2:])

    @staticmethod
    def to_hexadecimal(decimal) -> str:
        """
        Convert to hexadecimal.
        """
        if decimal > 0:
            hexadecimal_digits = []
            while decimal > 0:
                remainder = decimal % 16
                if remainder < 10:
                    hexadecimal_digits.insert(0, str(remainder))
                else:
                    hexadecimal_digits.insert(0, chr(ord('A') + (remainder - 10)))
                decimal = decimal // 16
            return ''.join(hexadecimal_digits)

        elif decimal == 0:
            return '0'

    @staticmethod
    def to_hexadecimal_builtin(decimal: int) -> str:
        """
        Convert to hexadecimal using the built-in hex() function.
        """
        return hex(abs(decimal))[2:]
