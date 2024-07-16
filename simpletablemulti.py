def multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
        limit = int(input("Enter the range (default is 10): ") or 10)
        multiplication_table(num, limit)
    except ValueError:
        print("Please enter valid integers.")
