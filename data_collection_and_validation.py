def get_user_info():
    full_name = input("Enter your full name: ").title().split() 
    for char in full_name:
        if char.isdigit():
            raise ValueError("Name can`t include numbers")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    show_only_initials = input("Would you like to get initials?(y/n): ").lower() == "y"
    mask_email = input("Would you like to mask email?(y/n): ").lower() == "y"
    encrypt_password = input("Would you like to encrypt password?(y/n): ").lower() == "y"
    valid_name = validate_name(full_name, show_only_initials)
    valid_email = validate_email(email, mask_email)
    valid_password = validate_password(password, encrypt_password)
    return valid_name, valid_email, valid_password

def validate_name(full_name: str, show_only_initials: bool) -> str:
    if len(full_name) < 2:
        raise ValueError("Wrong input. Must contain at least two words")
    else:
        for word in full_name:
            if len(word) < 2:
                raise ValueError("Wrong input. Each part must be at least 2 characters long")        
        if show_only_initials:
            user_initials = " ".join([word[0] for word in full_name])
            return f"Initials: {user_initials}"
        else: 
           return f"Full name: {full_name}"

def validate_email(email: str, mask_email: bool) -> str:
    if len(email) < 15:
        raise ValueError("Email must not be empty and must be at least 15 characters long")
    if not email.endswith((".com", ".org", "ua")):
        raise ValueError("Must end with '.com', '.org', or '.ua'")
    else:
        mask_email_name, user_domain = email.split("@")
    if mask_email:
        if len(mask_email_name) > 2:
            mask_email_name = mask_email_name[0] + "*"*(len(mask_email_name)-2) + mask_email_name[-1]                                                                                             
            return f"Masked email: {mask_email_name}@{user_domain}"
    else:
        return f"Unmasked email: {email}"

def validate_password(password: str, encrypt_password: bool) -> str:
    if len(password) < 8:
        raise ValueError("Minimum length: 8 characters")
    digit = False
    for char in password:
        if char.isdigit():
            digit = True
            break  
    if not digit:
        raise ValueError("Must contain at least one digit")
    uppercase_letter = False
    for char in password:
        if char.isupper():
            uppercase_letter = True
            break
    if not uppercase_letter:
        raise ValueError("Must contain at least one uppercase letter")
    if encrypt_password:
        reverse_password = password[::-1]
        return f"Encrypt password: {reverse_password}"
    else:
        return f"Unencrypt password: {password}"

def main() -> None:
    print("Welcome to the program \n")
    valid_name, valid_email, valid_password = get_user_info()
    print(valid_name)
    print(valid_email)
    print(valid_password)
      
if __name__ == "__main__":
    main()
        