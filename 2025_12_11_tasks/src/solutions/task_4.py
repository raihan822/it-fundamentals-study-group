"""
# Q4: Ask the user’s name and print:
    “Hello, <name>, welcome to our study group!”
"""
def greet_user(username: str) -> str:
    return f"Hello, {username}, welcome to our study group!"

if __name__ == "__main__":
    name: str = input("Enter your name: ")
    greet_msg: str = greet_user(name)
    print(greet_msg)