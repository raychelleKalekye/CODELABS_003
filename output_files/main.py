# main.py

import pandas as pd
import os
from generate_email import generate_email_addresses

def main():
    # Define the file path
    file_path = r'C:\Users\KE\Downloads\Test Files.xlsx'
    output_dir = 'output_files'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the Excel file
    try:
        all_sheets = pd.read_excel(file_path, sheet_name=None)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
        return

    for sheet_name, df in all_sheets.items():
        print(f"Processing Sheet: {sheet_name}")

        # Ensure the DataFrame contains the expected column
        if 'Student Name' not in df.columns:
            print(f"Error: 'Student Name' column not found in sheet '{sheet_name}'")
            continue

        try:
            emails = generate_email_addresses(df)
            df['Email'] = emails

            # Save to CSV file
            csv_output_file = os.path.join(output_dir, f'{sheet_name}_with_emails.csv')
            df.to_csv(csv_output_file, index=False)
            print(f"CSV saved to {csv_output_file}")

            # Save to TSV file
            tsv_output_file = os.path.join(output_dir, f'{sheet_name}_with_emails.tsv')
            df.to_csv(tsv_output_file, sep='\t', index=False)
            print(f"TSV saved to {tsv_output_file}")

        except Exception as e:
            print(f"Error processing sheet '{sheet_name}': {e}")

if __name__ == "__main__":
    main()
