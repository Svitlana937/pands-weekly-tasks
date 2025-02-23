def mask_account_number(account_number: str) -> str:
    """
    Masks all but the last 4 characters of an account number with 'X's.
    
    Assumptions:
    - The account number can be of any length.
    - If the account number is shorter than 4 characters, no masking is applied.
    
    Args:
        account_number (str): The account number of any length.
    
    Returns:
        str: The masked account number.
    """
    if len(account_number) <= 4:
        return account_number  # No masking needed for short numbers
    
    return 'X' * (len(account_number) - 4) + account_number[-4:]

if __name__ == "__main__":
    user_input = input("Enter an account number: ")
    masked_account = mask_account_number(user_input)
    print(f"Masked account number: {masked_account}")