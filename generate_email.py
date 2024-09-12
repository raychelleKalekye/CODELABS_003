# functions.py

import re

def generate_email_addresses(df):
    """Generate unique email addresses from a DataFrame of student names."""
    emails = []
    seen_emails = set()

    for name in df['Student Name']:
        # Split the name into last name and first/middle names
        if ',' in name:
            last_name, first_middle_names = name.split(',', 1)
        else:
            # In case the name is not formatted as expected
            last_name, first_middle_names = name, ""

        # Remove extra spaces and split the first and middle names
        first_middle_names = first_middle_names.strip().split()

        # Extract the first letter of the first name and the last name
        if len(first_middle_names) > 0:
            first_name_letter = first_middle_names[0][0].lower()
        else:
            first_name_letter = ''  # Handle cases where first/middle names are missing

        # Clean the last name and first name letter by removing non-alphanumeric characters
        last_name_clean = re.sub(r'[^a-zA-Z0-9]', '', last_name.strip()).lower()
        first_name_letter_clean = re.sub(r'[^a-zA-Z0-9]', '', first_name_letter)

        # Construct the base email (first letter of first name + last name)
        base_email = f"{first_name_letter_clean}{last_name_clean}@gmail.com"

        # Ensure uniqueness by appending a number if necessary
        email = base_email
        counter = 1
        while email in seen_emails:
            email = f"{first_name_letter_clean}{last_name_clean}{counter}@gmail.com"
            counter += 1

        seen_emails.add(email)
        emails.append(email)

    return emails
