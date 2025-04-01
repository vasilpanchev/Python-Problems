from typing import List


def crack_pincode(pincode: str) -> List[str]:
    adjacency_map = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9']
    }

    def generate_combinations(possible_digits):
        if not possible_digits:
            return ['']
        current_digits = possible_digits[0]
        remaining_combinations = generate_combinations(possible_digits[1:])
        return [digit + combo for digit in current_digits for combo in remaining_combinations]

    possible_digits = [adjacency_map[d] for d in pincode]
    result = generate_combinations(possible_digits)
    return result


n = input()
print(crack_pincode(n))
