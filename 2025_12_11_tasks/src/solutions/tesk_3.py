"""
# Q3: Take the user's birth year and calculate their age.
"""
def calculate_age(birth_year: int) -> int:
    import datetime
    current_year = datetime.datetime.now().year
    age_count = current_year - birth_year
    return age_count
if __name__ == "__main__":
    """instruction of use:
       Enter Birth year in integer number:
        i.e: 2000
        get result in integer Year: 25
    """

    birth_year_input: int = int(input("Enter you Birth Year: "))
    age: int = calculate_age(birth_year_input)

    print(f"Your Birth Year:{birth_year_input} \nYour age is: {age} Years")