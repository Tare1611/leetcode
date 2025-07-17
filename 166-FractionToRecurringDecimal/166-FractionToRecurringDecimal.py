# Last updated: 7/16/2025, 8:14:56 PM
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        # Convert to absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)  # No decimal part

        result.append(".")
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                # Insert '(' at the index where the repeating part starts
                insert_index = remainder_map[remainder]
                result.insert(insert_index, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)