def sum(*numbers: int) -> int:
    total: int = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    user_input: str = input("Enter two numbers: ")
    numbers: list = list(map(int, user_input.split(" ")))   # from map object to list conversion with list_comprehension

    sum = sum(*numbers)
    print(f"The total of the number {numbers} is = {sum}")