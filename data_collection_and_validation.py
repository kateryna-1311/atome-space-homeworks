
full_name = None
email = None
password = None
show_only_initials = None
mask_email = None
encrypt_password = None

def get_user_info(full_name, email, password, show_only_initials, mask_email, encrypt_password) -> tuple[str, str, str, bool, bool, bool]:
    full_name = input("Enter your full name: ").title().split() 
    for char in full_name:
        if char.isdigit():
            raise ValueError("Name can`t include numbers")
        
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    show_only_initials = input("Would you like to get initials?(y/n): ").lower()
    mask_email = input("Would you like to mask email?(y/n): ").lower()
    encrypt_password = input("Would you like to encrypt password?(y/n): ").lower()

    if show_only_initials == "y": 
        show_only_initials = True
    else:
        show_only_initials = False
    
    if mask_email == "y": 
        mask_email = True
    else:
        mask_email = False

    if encrypt_password == "y": 
        encrypt_password = True
    else:
        encrypt_password = False

    return full_name, email, password, show_only_initials, mask_email, encrypt_password

def validate_name(full_name: str, show_only_initials: bool) -> str:
        

    if len(full_name) < 2:
        raise ValueError("Wrong input. Must contain at least two words")
    else:
        for word in full_name:
            if len(word) < 2:
                raise ValueError("Wrong input. Each part must be at least 2 characters long")
        
        if show_only_initials:
            user_initials = " ".join([word[0] for word in full_name])
            print(f"Initials: {user_initials}")
        else: 
            print(f"Full name: {full_name}")

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
            print(f"Masked email: {mask_email_name}@{user_domain}")
    else:
        print(f"Unmasked email: {email}")

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
        print(f"Encrypt password: {reverse_password}")
    else:
        print(f"Unencrypt password: {password}")

def main() -> None:

    global full_name, email, password, show_only_initials, mask_email, encrypt_password
    print("Welcome to the program \n")

    full_name, email, password, show_only_initials, mask_email, encrypt_password = get_user_info(full_name, email, password, show_only_initials, mask_email, encrypt_password)
    validate_name(full_name, show_only_initials)
    validate_email(email, mask_email)
    validate_password(password, encrypt_password)  

if __name__ == "__main__":
    main()
        