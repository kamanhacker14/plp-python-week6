def ask_for_number():
    while True:
        text = input("Enter a whole number: ")
        try:
            return int(text)
        except ValueError:
            print("That is not a number. Try again.")


def main():
    number = ask_for_number()
    try:
        print(100 / number)
    except ZeroDivisionError:
        print("Cannot divide by zero")


main()
