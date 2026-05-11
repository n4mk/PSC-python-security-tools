def checkStrength(password):

    has_length = len(password) >=8
    has_symbols = any(not c.isalnum() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    
    score = 0
    if has_length:
        score +=1
    if has_symbols:
        score +=1
    if has_number:
        score +=1
    if has_upper:
        score +=1
    if has_lower:
        score +=1
    if score <= 2:
        return "weak"
    elif score <= 4:
        return "medium"
    else:
        return "strong"


if __name__=="__main__":
    while True:
        print("Password Strength Checker")
        user_password = input("Enter Password to Check: ")
        if not user_password.lower() == "exit":
            print("Exiting Password Checker")
            break
        result = checkStrength(user_password)
        print(f"Result: {result}")
