import re


class Binary:
    """
    Convert binary to decimal, octal and hexadecimal.
    """

    @staticmethod
    def is_binary(text: str) -> bool:
        """
        Check if a string represents a valid binary number.
        """
        return re.match('^[01]+$', text) is not None

    @staticmethod
    def to_decimal(binary: str) -> int:
        """
        Convert to decimal.
        """
        if Binary.is_binary(binary):
            decimal = 0
            for index, value in enumerate(binary[::-1]):
                if value == '1':
                    decimal += 2 ** index
            return decimal

    @staticmethod
    def to_decimal_builtin(binary: str) -> int:
        """
        Convert to decimal using the built-in int() function.
        """
        if Binary.is_binary(binary):
            return int(binary, 2)

    @staticmethod
    def to_octal(binary: str) -> str:
        """
        Convert to octal using the built-in oct() function.
        """
        if Binary.is_binary(binary):
            return oct(int(binary, 2))[2:]

    @staticmethod
    def to_hexadecimal(binary: str) -> str:
        """
        Convert to hexadecimal using the built-in hex() function.
        """
        if Binary.is_binary(binary):
            return hex(int(binary, 2))[2:]
