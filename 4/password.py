def main():
    # possible_passwords = ['111111', '112233', '223450', '123789', '123444', '111122']
    possible_passwords = [password for password in range(138241, 674035)]
    possible_passwords = filter_always_increasing_digits(possible_passwords)
    possible_passwords = filter_two_adjacent(possible_passwords)

    return len(possible_passwords)

def filter_always_increasing_digits(passwords):
    filtered = []
    for password in passwords:
        password_str = str(password)
        for i, digit in enumerate(password_str):
            try:
                if password_str[i] > password_str[i+1]:
                    break
            except:
                filtered.append(password)

    return filtered

def filter_two_adjacent(passwords):
    filtered = []
    for password in passwords:
        if is_password(password):
            filtered.append(password)

    return filtered

def is_password(password):
    password_str = str(password)
    bad_digit = None
    for i, digit in enumerate(password_str):
        if digit == bad_digit:
            continue

        try:
            if password_str[i] == password_str[i+1] and password_str[i] == password_str[i+2]:
                bad_digit = password_str[i]
                continue
            if password_str[i] == password_str[i+1]:
                return True
        except IndexError:
            try:
                if (password_str[i] == password_str[i+1]):
                    return True
            except IndexError:
                pass

    return False

if __name__ == "__main__":
    print(main())
