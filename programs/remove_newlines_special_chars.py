import re
import os
from pathlib import Path

def clean_markdown_file(input_md_path, output_path=None, keep_alphanumeric_only=True):
    """
    Remove special characters from markdown file and replace newlines with spaces
    
    Args:
        input_md_path (str): Path to input markdown file
        output_path (str): Path to output file (optional)
        keep_alphanumeric_only (bool): If True, keeps only letters, numbers, and spaces
    """
    try:
        # Validate input file
        if not os.path.exists(input_md_path):
            raise FileNotFoundError(f"Markdown file '{input_md_path}' not found")
        
        # Generate output path if not provided
        if output_path is None:
            base_name = Path(input_md_path).stem
            output_path = f"{base_name}_cleaned.txt"
        
        # Read markdown file
        with open(input_md_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Process content
        cleaned_content = remove_special_characters(content, keep_alphanumeric_only)
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        
        print(f"✅ Successfully cleaned markdown file: {input_md_path}")
        print(f"📁 Output saved to: {output_path}")
        print(f"📊 Original length: {len(content)} characters")
        print(f"📏 Cleaned length: {len(cleaned_content)} characters")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Error processing markdown file: {e}")
        return None

def remove_special_characters(content, keep_alphanumeric_only=True):
    """
    Remove special characters and replace newlines with spaces
    
    Args:
        content (str): Input text content
        keep_alphanumeric_only (bool): Keep only alphanumeric characters and spaces
    
    Returns:
        str: Cleaned content
    """
    # Step 1: Replace all types of newlines with single space
    content = content.replace('\n', ' ').replace('\r', ' ').replace('\r\n', ' ')
    
    if keep_alphanumeric_only:
        # Step 2: Keep only alphanumeric characters and spaces
        cleaned_content = re.sub(r'[^a-zA-Z0-9\s]', '', content)
    else:
        # Step 2: Remove common special characters but keep basic punctuation
        cleaned_content = re.sub(r'[^\w\s\.\,\!\?\-]', '', content)
    
    # Step 3: Clean up multiple consecutive spaces
    cleaned_content = re.sub(r'\s+', ' ', cleaned_content)
    
    # Step 4: Strip leading/trailing whitespace
    cleaned_content.strip()

    # Step 5: Keep only first 256 characters
    #cleaned_content = cleaned_content[:256]

    return cleaned_content

# Usage
clean_markdown_file(r'C:\Users\rudra\Documents\coding-projects\aws-genai-llm-chatbot\prompts\hr_assistant_prompt.md', r'C:\Users\rudra\Documents\coding-projects\aws-genai-llm-chatbot\prompts\hr_assistant_prompt_singleline.txt', keep_alphanumeric_only=True)
