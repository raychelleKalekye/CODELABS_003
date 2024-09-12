import pandas as pd
import os
import json

def shuffle_and_save_json(output_dir):
    # Load the merged student list
    merged_file = os.path.join(output_dir, 'merged_students.csv')
    merged_df = pd.read_csv(merged_file)

    # Shuffle the merged DataFrame
    shuffled_df = merged_df.sample(frac=1).reset_index(drop=True)

    # Save the shuffled data as a JSON file
    shuffled_file = os.path.join(output_dir, 'shuffled_students.json')
    shuffled_df.to_json(shuffled_file, orient='records', lines=False)
    print(f"Shuffled JSON saved to {shuffled_file}")

def save_jsonl_with_format(output_dir):
    # Load the merged student list
    merged_file = os.path.join(output_dir, 'merged_students.csv')
    merged_df = pd.read_csv(merged_file)

    jsonl_data = []

    # Loop through each row and format according to the example
    for i, row in merged_df.iterrows():
        record = {
            "id": str(i),
            "student_number": row['Student Number'],
            "additional_details": [
                {
                    "dob": str(row['DoB']),
                    "gender": row['Gender'].lower(),
                    "special_character": "['yes']" if "'" in row['Student Name'] else "['no']",  # Logic for special characters
                    "name_similar": "['no']"  # Placeholder for name similarity (you can adjust this logic if needed)
                }
            ]
        }
        jsonl_data.append(record)

    # Save the formatted data as a JSONL file with indentation
    jsonl_file = os.path.join(output_dir, 'students_formatted.jsonl')
    with open(jsonl_file, 'w') as f:
        for record in jsonl_data:
            json.dump(record, f, indent=4)  # Using indent=4 for proper formatting
            f.write('\n')  # Add a new line after each record for proper JSONL format

    print(f"Formatted JSONL saved to {jsonl_file}")

if __name__ == "__main__":
    output_dir = 'output_files'
    shuffle_and_save_json(output_dir)  # First, save the shuffled JSON
    save_jsonl_with_format(output_dir)  # Then, save the formatted JSONL
