"""
# Q2: Ask the user for temperature in Celsius and print it in Fahrenheit
```Formula: (C * 9/5) + 32```
"""

def convert_celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5)+32

if __name__ == "__main__":
    """instruction of use:
    Enter celcius value in int or float number:
    i.e: 30
    get result in fahrenheit as: 86.0
    """

    celsius: float = float(input("Enter celcius value: "))
    result: float = convert_celsius_to_fahrenheit(celsius)

    print(f"{celsius} degree celsius is equivalent to ==> \n{result} degree fahrenheit")