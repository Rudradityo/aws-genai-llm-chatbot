import re

# Define the set of special characters in Markdown
special_chars = r'\\|\`|\*|_|{|}|\[|\]|\(|\)|#|\+|-|\.|!|>|~|\^|:|\|'

def extract_special_characters_from_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all special characters
    matches = re.findall(special_chars, content)
    # Return unique special characters as a concatenated string
    return ''.join(set(matches))

# Example usage:
special_characters = extract_special_characters_from_markdown(r'C:\Users\rudra\Documents\coding-projects\aws-genai-llm-chatbot\prompts\hr_assistant_prompt.md')
print(special_characters)