"""
# **Task_6: Personal Information Card (Python)**

**Requirements:**
1. Ask the user:

   * Name
   * Age
   * Favorite color
   * Hobby
2. Store them in variables
3. Print in this format:

#----- Personal Info Card -----
Name:
Age:
Favorite Color:
Hobby:
--------------------------------
"""
def personal_info_card(name: str, age: int, fav_color: str, hobby: str) -> str:
    info_card: str = f"""#----- Personal Info Card -----
Name:   {name}
Age:    {age}
Favorite Color: {fav_color}  
Hobby:  {hobby}
--------------------------------"""
    return info_card

if __name__ == "__main__":
    usr_name: str = input("Enter Your Name: ")
    usr_age: int = int(input("Enter Your Age: "))
    usr_fav_color: str = input("Enter Your Favorite Color: ")
    usr_hobby: str = input("Enter Your Hobbies: ")

    #====================================
    import time
    import random
    sleep_duration: float = random.uniform(2.1,5)
    print(f"Decorating your card... please wait {sleep_duration:.1f}s")
    time.sleep(sleep_duration)
    print("Done! Your Card is Ready!\n\n")
    #====================================

    msg = personal_info_card(usr_name, usr_age, usr_fav_color, usr_hobby)
    print(msg)