import csv

def analyze_richest_people(file_path):
    """
    Analyzes a CSV file containing information about fictional richest people
    to answer specific questions.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing:
            - dict: A dictionary with the details of the richest person (Name, Net Worth, Email, Phone Number).
                    Returns None if no richest person is found or an error occurs.
            - int: The count of people without an email.
            - int: The count of people without a phone number.
    """
    richest_person_details = None # Will store the dictionary of the richest person's details
    max_net_worth = -1
    people_without_email = 0
    people_without_phone = 0

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Check if headers exist and are as expected
            if not reader.fieldnames:
                print("Error: CSV file is empty or has no headers.")
                return None, 0, 0

            # Expected headers (case-sensitive)
            expected_headers = ['Name', 'Net Worth', 'Email', 'Phone Number']
            if not all(header in reader.fieldnames for header in expected_headers):
                print(f"Error: Missing one or more expected headers. Found: {reader.fieldnames}, Expected: {expected_headers}")
                return None, 0, 0

            for row in reader:
                # 1. Find the richest person
                try:
                    # UPDATED: Remove 'billion' and 'million' before converting to int
                    net_worth_str = row['Net Worth'].replace('$', '').replace(',', '').replace(' billion', '000000000').replace(' million', '000000').strip()
                    net_worth = int(net_worth_str)
                    if net_worth > max_net_worth:
                        max_net_worth = net_worth
                        # Store the entire row for the richest person
                        richest_person_details = {
                            'Name': row.get('Name'),
                            'Net Worth': row.get('Net Worth'),
                            'Email': row.get('Email'),
                            'Phone Number': row.get('Phone Number')
                        }
                except ValueError:
                    print(f"Warning: Could not parse net worth for {row.get('Name', 'Unknown')}: '{row['Net Worth']}'. Skipping for richest person calculation.")
                    pass # Skip if net worth is not a valid number

                # 2. Count people without an email
                if not row['Email'] or row['Email'].strip() == '':
                    people_without_email += 1

                # 3. Count people without phone numbers
                if not row['Phone Number'] or row['Phone Number'].strip() == '':
                    people_without_phone += 1

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None, 0, 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, 0, 0

    return richest_person_details, people_without_email, people_without_phone

# Define the file path for the uploaded CSV
file_path = "fictional_richest_people.csv"

# Analyze the file
richest_person_info, no_email_count, no_phone_count = analyze_richest_people(file_path)

# Print the results
if richest_person_info is not None:
    print(f"1. The richest person is {richest_person_info.get('Name', 'N/A')} with a net worth of {richest_person_info.get('Net Worth', 'N/A')}")
    print(f"2. Number of people without an email: {no_email_count}")
    print(f"3. Number of people without phone numbers: {no_phone_count}")
else:
    print("Could not complete the analysis due to errors.")
