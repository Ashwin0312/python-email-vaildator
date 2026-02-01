from colorama import Fore, Style, init
init(autoreset=True)

# ===================== FUNCTION =====================
def validate_email(email):
    """
    Validates an email address for:
    - Length
    - First character
    - '@' symbol
    - Allowed domains
    - Spaces
    - Uppercase letters
    - Consecutive dots
    - Invalid special characters
    """
    errors = []
    allowed_domains = ('.com', '.in', '.org', '.net', '.edu', '.co')

    # 1️⃣ Length Check
    if len(email) < 6:
        errors.append("must be at least 6 characters long.")

    # 2️⃣ First Character Check
    if not email[0].isalpha():
        errors.append("first character must be a letter.")

    # 3️⃣ '@' Symbol Check
    if email.count('@') != 1:
        errors.append("must contain exactly one '@' symbol.")

    # 4️⃣ Domain Check
    if not any(email.endswith(ext) for ext in allowed_domains):
        errors.append("unsupported domain extension (use .com, .in, .org, .net, .edu, .co).")

    # 5️⃣ Character Validation
    has_uppercase = False
    has_invalid_char = False
    has_space = False

    for ch in email:
        if ch.isspace():
            has_space = True
        elif ch.isalpha():
            if ch.isupper():
                has_uppercase = True
        elif ch.isdigit() or ch in ['_', '.', '@']:
            continue
        else:
            has_invalid_char = True

    if has_space:
        errors.append("contains space.")
    if has_uppercase:
        errors.append("contains uppercase letters.")
    if has_invalid_char:
        errors.append("contains invalid special characters.")

    # 6️⃣ Consecutive dots check
    if ".." in email:
        errors.append("contains consecutive dots ('..').")

    # ✅ Print Results
    if errors:
        print(Fore.LIGHTRED_EX + "\n⚠️ Invalid Email:")
        for e in set(errors):
            print(Fore.YELLOW + " - " + e)
        return False
    else:
        # Valid email now in RED
        print(Fore.RED + f"\n✅ Valid Email: {email}")
        return True

# ===================== MAIN PROGRAM =====================
# Title in yellow
print(Fore.YELLOW + "✨ Welcome to the Smart Email Validator ✨\n")

# Instructions in green
instruction_color = Fore.GREEN
print(instruction_color + "Instructions:")
print(instruction_color + "- Enter your email to check validity")
print(instruction_color + "- Examples: example123@gmail.com, user.name@outlook.in, tanishk.jain@s.amity.edu")
print(instruction_color + "- Type 'exit' to quit the program\n")

# Input prompt in blue
prompt_color = Fore.BLUE

while True:
    user_input = input(prompt_color + "Enter your Email: " + Style.RESET_ALL).strip()
    if user_input.lower() == 'exit':
        print(Fore.LIGHTMAGENTA_EX + "\n👋 Thank you for using the Email Validator. Goodbye!")
        break
    validate_email(user_input)
    print(Style.RESET_ALL)
