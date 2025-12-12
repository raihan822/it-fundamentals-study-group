"""
# Mini Project (Beginner): “Simple Calculator”
Features:
    Take 2 inputs
    Add, subtract, multiply, divide
    Print results

```This helps everyone learn variables + operations + user input```
"""
def calculator(x: float, y: float, op: int) ->float | None:
    match op:
        case 1: return x+y
        case 2: return x-y
        case 3: return x*y
        case 4:
            try:
                if y == 0:
                    raise ZeroDivisionError("Division by Zero!")
                return x/y
            except Exception as e:
                print(e)
                return None
        case _: #default case!
            # unreachable on this module, as Already did input verification! but kept if used from else where!
            print(f"Undefined Operation: {op}!!")
            return None


if __name__ == "__main__":
    try:
        input_numbers: str = input("Enter two numbers (separated by Space): ")
        numbers = list(map(float, input_numbers.split(" ")))  # print(input_numbers.split(" ")) # this separates on space and returns a list
        if len(numbers) != 2:
            raise ValueError("Please enter exactly two numbers (separated by Space).")

        input_operation: int = int(input(
            """Enter Operation No. to perform (i.e: 2):
        1. Add 
        2. subtract
        3. multiply
        4. divide
        ==> """
        ))
        if not (1 <= input_operation <= 4):
            raise ValueError("Operation Selection out of range!")
    except Exception as e:
        print(e)
        exit()


    result = calculator(*numbers, input_operation)
    if result is not None:
        signs: dict[int, str] = {1: '+', 2: '-', 3: '*', 4: '/'}
        op_symbol: str = signs[input_operation]
        print(f"Result: \n{numbers[0]} {op_symbol} {numbers[1]} = {result}")