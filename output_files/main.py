# main.py

import pandas as pd
import os
from generate_email import generate_email_addresses
from functions import get_special_characters_students
from similarity import compute_similarity_matrix, save_similarity_results


def main():
    # Define the file path
    file_path = r'../input_files/Test Files.xlsx'
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

            # Separate male and female students
            male_students = df[df['Gender'] == 'M']
            female_students = df[df['Gender'] == 'F']

            # Save Male and Female lists to separate files
            male_file = os.path.join(output_dir, f'{sheet_name}_male_students.csv')
            female_file = os.path.join(output_dir, f'{sheet_name}_female_students.csv')
            male_students.to_csv(male_file, index=False)
            female_students.to_csv(female_file, index=False)
            print(f"Male students saved to {male_file}")
            print(f"Female students saved to {female_file}")

            # Identify and save students with special characters
            special_char_students = get_special_characters_students(df)
            special_char_file = os.path.join(output_dir, f'{sheet_name}_special_char_students.csv')
            special_char_students.to_csv(special_char_file, index=False)
            print(f"Special characters students saved to {special_char_file}")

            # Log counts of male and female students
            import logging

            log_file_path = os.path.join(output_dir, 'students.log')
            logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')
            logging.info(f"Number of male students in {sheet_name}: {len(male_students)}")
            logging.info(f"Number of female students in {sheet_name}: {len(female_students)}")

            # Separate male and female names for similarity analysis
            male_names = male_students['Student Name'].tolist()
            female_names = female_students['Student Name'].tolist()

            # Compute and save similarity results
            if male_names and female_names:
                similarity_matrix = compute_similarity_matrix(male_names, female_names)
                save_similarity_results(male_names, female_names, similarity_matrix, threshold=0.5)

        except Exception as e:
            print(f"Error processing sheet '{sheet_name}': {e}")

if __name__ == "__main__":
    main()
