"""Coding Game: Challange 2"""


def get_navigation_value_from_file(_filename):
    """PYLINT, STOP COMPLAINING"""
    with open(_filename, 'r', encoding="utf-8") as file:
        value_data = list(map(int, file.read().strip().split()))

    # Filter out values that don't adhere to even parity
    even_parity_values = [x for x in value_data if bin(x).count('1') % 2 == 0]

    if len(even_parity_values) == 0:
        return "No valid navigation value found."

    # Remove the parity bit from each value and calculate the average
    no_parity_values = [(x & ~(1 << 15)) for x in even_parity_values]
    average_value = round(sum(no_parity_values) / len(no_parity_values))

    return average_value


FILENAME = "Challenge 2/data"
result = get_navigation_value_from_file(FILENAME)
print(result)
