import re

def find_special_characters(name):
    return bool(re.search(r"[^\w\s,]", name))

def get_special_characters_students(df):
    """Identify students with special characters in their names."""
    df['Special Characters'] = df['Student Name'].apply(find_special_characters)
    special_char_students = df[df['Special Characters']]
    return special_char_students


