import re

def check_password_strength(password):
    
    length_ok = len(password) >= 9 
    
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[^A-Za-z0-9]', password) is not None  
    
    conditions_met = sum([length_ok, has_uppercase, has_lowercase, has_digit, has_special])
    
    if conditions_met == 5:
        return "Very Strong"
    elif conditions_met == 4:
        return "Strong"
    elif conditions_met == 3:
        return "Moderate"
    elif conditions_met == 2:
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"The strength of the password '{password}' is: {strength}")
