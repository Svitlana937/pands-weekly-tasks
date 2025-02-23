def convert_to_cents(amount: float) -> int:
    return abs(int(round(amount * 100)))

if __name__ == "__main__":
    user_input = float(input("Please enter the amount: "))
    cents = convert_to_cents(user_input)
    print(f"That amount in cents is: {cents}")