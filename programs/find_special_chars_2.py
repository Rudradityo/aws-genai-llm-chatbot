import os
import string

def read_markdown_special_chars(filename):
    """
    Read a markdown file character by character and extract special characters.
    
    Args:
        filename (str): Path to the markdown file
    
    Returns:
        set: Set of unique special characters found in the file
    """
    special_chars_list = []
    
    try:
        # Check if file exists
        if not os.path.isfile(filename):
            print(f"Error: File '{filename}' not found.")
            return set()
        
        # Open file in read mode with UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"Reading file: {filename}")
            
            # Read character by character
            while True:
                char = file.read(1)
                
                # Break if end of file
                if not char:
                    break
                
                # Check if character is a special character
                # Special characters are non-alphanumeric and non-whitespace
                if not char.isalnum() and not char.isspace():
                    special_chars_list.append(char)
        
        # Convert list to set to get unique characters
        special_chars_set = set(special_chars_list)
        
        return special_chars_set
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return set()

def main():
    # Get filename from user input
    filename = input("Enter the markdown file path: ").strip()
    
    # Alternative: Use a default filename for testing
    # filename = "example.md"
    
    # Read special characters from the file
    special_chars = read_markdown_special_chars(filename)
    
    # Print results
    if special_chars:
        print(f"\nUnique special characters found: {len(special_chars)}")
        print("Special characters set:")
        print(special_chars)

        # Print sorted for better readability
        print("\nSorted special characters in string:")
        print(''.join(sorted(special_chars)))
    else:
        print("No special characters found or file could not be read.")

# Alternative version with predefined special characters
def read_markdown_with_predefined_specials(filename):
    """
    Alternative version that checks against predefined special characters
    commonly found in markdown files.
    """
    # Define common markdown special characters
    markdown_specials = set('*_`~[](){}#+-=|\\<>!.:;,?/^&@$%')
    
    special_chars_list = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                
                # Check if character is in our predefined set
                if char in markdown_specials:
                    special_chars_list.append(char)
        
        return set(special_chars_list)
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return set()

if __name__ == "__main__":
    main()
