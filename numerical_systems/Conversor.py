import re


class Conversor:

    @staticmethod
    def is_binary(text: str) -> bool:
        """
        Check if a string represents a binary number.
        """
        return re.match('^[01]+$', text) is not None

    @staticmethod
    def binary_to_decimal(binary: str) -> int | None:
        """
        Converts a binary number into a decimal number.
        """
        if Conversor.is_binary(binary):
            decimal = 0
            for index, value in enumerate(binary[::-1]):
                if value == '1':
                    decimal += 2 ** index
            return decimal
        else:
            return None

    @staticmethod
    def binary_to_octal(binary: str) -> str | None:
        """
        Converts a binary number into an octal number.
        """
        if Conversor.is_binary(binary):
            return oct(int(binary, 2))[2:]
        else:
            return None

    @staticmethod
    def binary_to_hexadecimal(binary: str) -> str | None:
        """
        Converts a binary number into a hexadecimal number.
        """
        if Conversor.is_binary(binary):
            return hex(int(binary, 2))[2:].upper()
        else:
            return None

    @staticmethod
    def decimal_to_binary(number: int) -> str | None:
        """
        Converts a decimal positive number into a binary number.
        """
        if number > 0:
            binary = []
            while number > 0:
                binary.insert(0, str(number % 2))
                number //= 2
            return ''.join(binary)
        elif number == 0:
            return '0'
        else:
            return None

    @staticmethod
    def decimal_to_octal(number: int) -> str | None:
        """
        Converts a decimal positive number into an octal number.
        """
        if number > 0:
            octal = []
            while number > 0:
                octal.insert(0, str(number % 8))
                number //= 8
            return ''.join(octal)
        elif number == 0:
            return '0'
        else:
            return None

    @staticmethod
    def decimal_to_hexadecimal(number: int) -> str | None:
        """
        Converts a decimal positive number into a hexadecimal number.
        """
        if number > 0:
            hexadecimal = []
            while number > 0:
                remainder = number % 16
                if remainder < 10:
                    hexadecimal.insert(0, str(remainder))
                else:
                    hexadecimal.insert(0, chr(ord('A') + (remainder - 10)))
                number //= 16
            return ''.join(hexadecimal)
        elif number == 0:
            return '0'
        else:
            return None

    @staticmethod
    def octal_to_decimal(octal: str) -> int:
        """
        Converts an octal number into a decimal number.
        """
        return int(octal, 8)

    @staticmethod
    def hexadecimal_to_decimal(hexadecimal: str) -> int:
        """
        Converts a hexadecimal number into a decimal number.
        """
        return int(hexadecimal, 16)
