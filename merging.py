import pandas as pd
import os

def merge_student_lists(output_dir):
    # Load male, female, and special character lists for both File_A and File_B
    male_students_A = pd.read_csv(os.path.join(output_dir, 'File_A_male_students.csv'))
    female_students_A = pd.read_csv(os.path.join(output_dir, 'File_A_female_students.csv'))
    special_char_students_A = pd.read_csv(os.path.join(output_dir, 'File_A_special_char_students.csv'))

    male_students_B = pd.read_csv(os.path.join(output_dir, 'File_B_male_students.csv'))
    female_students_B = pd.read_csv(os.path.join(output_dir, 'File_B_female_students.csv'))
    special_char_students_B = pd.read_csv(os.path.join(output_dir, 'File_B_special_char_students.csv'))

    # Combine A and B for each category
    male_students = pd.concat([male_students_A, male_students_B]).drop_duplicates()
    female_students = pd.concat([female_students_A, female_students_B]).drop_duplicates()
    special_char_students = pd.concat([special_char_students_A, special_char_students_B]).drop_duplicates()

    # Combine all into one DataFrame
    merged_df = pd.concat([male_students, female_students, special_char_students]).drop_duplicates()

    # Ensure "Email Address" is part of the merge
    if 'Email' in merged_df.columns:
        merged_df = merged_df[['Student Number', 'Student Name', 'DoB', 'Email', 'Gender']]
    else:
        print("Error: 'Email' column not found in the merged data.")

    # Save the merged file
    merged_file = os.path.join(output_dir, 'merged_students.csv')
    merged_df.to_csv(merged_file, index=False)
    print(f"Merged data saved to {merged_file}")

if __name__ == "__main__":
    output_dir = 'output_files'
    merge_student_lists(output_dir)
