import random
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("  [!] You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    suggestions = []

    # Length scoring
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters (12+ is ideal)")

    # Character variety scoring
    if has_upper:
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z)")

    if has_lower:
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z)")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add digits (0-9)")

    if has_symbol:
        score += 1
    else:
        suggestions.append("Add symbols (!@#$...)")

    # Classify strength
    if score <= 2:
        strength = "Weak 🔴"
    elif score <= 4:
        strength = "Medium 🟡"
    else:
        strength = "Strong 🟢"

    # Display results
    print("\n  ── Password Analysis ──────────────────────")
    print(f"  Length       : {length} characters")
    print(f"  Uppercase    : {'✔' if has_upper else '✘'}")
    print(f"  Lowercase    : {'✔' if has_lower else '✘'}")
    print(f"  Digits       : {'✔' if has_digit else '✘'}")
    print(f"  Symbols      : {'✔' if has_symbol else '✘'}")
    print(f"  Score        : {score}/6")
    print(f"  Strength     : {strength}")

    if suggestions:
        print("\n  💡 Suggestions to improve your password:")
        for s in suggestions:
            print(f"     • {s}")
    else:
        print("\n  ✅ Great password! No improvements needed.")
    print("  ────────────────────────────────────────────")


def generator_menu():
    print("\n  ── Generate Password ────────────────────────")
    while True:
        try:
            length = int(input("  Enter desired password length (4-64): "))
            if 4 <= length <= 64:
                break
            print("  [!] Please enter a number between 4 and 64.")
        except ValueError:
            print("  [!] Invalid input. Enter a whole number.")

    use_letters = input("  Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("  Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("  Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"\n  ✅ Generated Password: {password}")
        # Auto-check strength of generated password
        print("\n  Checking strength of generated password...")
        check_strength(password)


def checker_menu():
    print("\n  ── Check Password Strength ──────────────────")
    password = input("  Enter the password to check: ")
    if not password:
        print("  [!] No password entered.")
        return
    check_strength(password)


def main():
    print("=" * 48)
    print("       🔐 Password Generator & Checker")
    print("=" * 48)

    while True:
        print("\n  MENU")
        print("  [1] Generate a new password")
        print("  [2] Check password strength")
        print("  [3] Exit")
        choice = input("\n  Choose an option (1/2/3): ").strip()

        if choice == '1':
            generator_menu()
        elif choice == '2':
            checker_menu()
        elif choice == '3':
            print("\n  Goodbye! Stay secure. 👋\n")
            break
        else:
            print("  [!] Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()