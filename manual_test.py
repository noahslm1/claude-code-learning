def main():
    try:
        name = input("What is your name? ")
        age_input = input("What is your age? ")
    except EOFError:
        print("No input received.")
        return

    try:
        age = int(age_input)
        if age <= 0:
            raise ValueError
        print(f"Hello {name}, you are {age} years old. Welcome to Claude Code! Have a great day!")
    except ValueError:
        print(f"Sorry {name}, '{age_input}' is not a valid age.")


if __name__ == "__main__":
    main()
