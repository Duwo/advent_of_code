def main():
    possible_passwords = ['111111', '223450', '123789']
    possible_passwords = [password for password in range(138241, 674035)]
    possible_passwords = filter_two_adjacent(possible_passwords)
    possible_passwords = filter_always_increasing_digits(possible_passwords)

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
        password_str = str(password)
        for i, digit in enumerate(password_str):
            try:
                if password_str[i] == password_str[i+1]:
                    filtered.append(password)
                    break
            except:
                pass

    return filtered


if __name__ == "__main__":
    print(main())
