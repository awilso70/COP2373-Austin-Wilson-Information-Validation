import re


# Function to validate phone number
def phone_validation(phone_number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'  # Pattern for a phone number in the format xxx-xxx-xxxx
    if re.match(pattern, phone_number):
        return True
    return False


# Function to validate social security number
def ssn_validation(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'  # Pattern for SSN in the format xxx-xx-xxxx
    if re.match(pattern, ssn):
        return True
    return False


# Function to validate zip code
def zip_validation(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'  # Pattern for zip code in the format xxxxx or xxxxx-xxxx
    if re.match(pattern, zip_code):
        return True
    return False


# Main function to get input from the user and display validation results
def main():
    phone_number = input("Enter your phone number (xxx-xxx-xxxx): ")
    ssn = input("Enter your Social Security Number (xxx-xx-xxxx): ")
    zip_code = input("Enter your ZIP code (xxxxx or xxxxx-xxxx): ")

    # Validate inputs and display results
    if phone_validation(phone_number):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    if ssn_validation(ssn):
        print("Social Security Number is valid.")
    else:
        print("Social Security Number is invalid.")

    if zip_validation(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


if __name__ == "__main__":
    main()