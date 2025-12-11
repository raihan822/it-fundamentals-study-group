"""
# Q1: Take two numbers as input and print their sum.
"""

def sum_numbers(*numbers: int) -> int:
    total: int = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    """instruction of use:
    Enter numbers separated by _space_:
    i.e: 5 6 8 7
    get result of 5 6 8 7 as: 26
    """

    user_input: str = input("Enter two numbers: ")
    numbers: list = list(map(int, user_input.split(" ")))   # from map object to list conversion with list_comprehension

    result: int = sum_numbers(*numbers)
    print(f"The total of the numbers {numbers} is = {result}")