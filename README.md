# Richest People Analysis

This project provides a Python script to parse a CSV file containing information about the world's richest people and answer specific questions about the data.

## Features

The program analyzes the provided CSV file and outputs the following information:

1.  **Richest Person:** Identifies the person with the highest net worth in the list.
2.  **People Without Email:** Counts the number of individuals whose email addresses are missing.
3.  **People Without Phone Numbers:** Counts the number of individuals whose phone numbers are missing.

## Usage

To run the program, you will need Python installed.

1.  **Save the CSV file:** Ensure your CSV file, named `fictional_richest_people.csv`, is in the same directory as the Python script.
2.  **Run the script:** Execute the Python script from your terminal:

    ```bash
    python Richest_People_Analysis.py
    ```

    (The script name is `Richest_People_Analysis.py`.)

## CSV File Format

The CSV file is expected to have the following columns:

* `Name`: The name of the person.
* `Net Worth (USD)`: The net worth of the person in US Dollars (numeric value).
* `Email`: The email address of the person (can be empty).
* `Phone Number`: The phone number of the person (can be empty).

**Example:**

```csv
Name,Net Worth (USD),Email,Phone Number
Elon Musk,210000000000,elon.musk@tesla.com,123-456-7890
Bernard Arnault & family,205000000000,,987-654-3210
Jeff Bezos,195000000000,jeff.bezos@amazon.com,
Larry Ellison,155000000000,larry.ellison@oracle.com,555-123-4567
Mark Zuckerberg,150000000000, ...................................
```

## Sample CSV Data

For your convenience, here is the sample `fictional_richest_people.csv` data that the script is designed to process:

```csv
Name,Net Worth (USD),Email,Phone Number
Elon Musk,210000000000,elon.musk@tesla.com,123-456-7890
Bernard Arnault & family,205000000000,,987-654-3210
Jeff Bezos,195000000000,jeff.bezos@amazon.com,
Larry Ellison,155000000000,larry.ellison@oracle.com,555-123-4567
Mark Zuckerberg,150000000000,,
Bill Gates,130000000000,bill.gates@microsoft.com,111-222-3333
Steve Ballmer,120000000000,,
Larry Page,115000000000,larry.page@google.com,444-555-6666
Sergey Brin,110000000000,,777-888-9999
Warren Buffett,100000000000,warren.buffett@berkshire.com, .........................................
