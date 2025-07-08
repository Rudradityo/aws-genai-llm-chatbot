import re
import os
from pathlib import Path

def process_markdown_file(input_md_path, output_path=None, preserve_formatting=False):
    """
    Process a markdown file to remove newlines
    
    Args:
        input_md_path (str): Path to input markdown file
        output_path (str): Path to output file (optional)
        preserve_formatting (bool): Whether to preserve some markdown formatting
    """
    try:
        # Validate input file
        if not input_md_path.endswith('.md'):
            print("⚠️  Warning: File doesn't have .md extension")
        
        if not os.path.exists(input_md_path):
            raise FileNotFoundError(f"Markdown file '{input_md_path}' not found")
        
        # Generate output path if not provided
        if output_path is None:
            base_name = Path(input_md_path).stem
            output_path = f"{base_name}_single_line.txt"
        
        # Read markdown file
        with open(input_md_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Process based on formatting preference
        if preserve_formatting:
            processed_content = process_markdown_preserve_structure(markdown_content)
        else:
            processed_content = process_markdown_simple(markdown_content)
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(processed_content)
        
        print(f"✅ Successfully processed markdown file: {input_md_path}")
        print(f"📁 Output saved to: {output_path}")
        print(f"📊 Original lines: {len(markdown_content.splitlines())}")
        print(f"📏 Final length: {len(processed_content)} characters")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Error processing markdown file: {e}")
        return None

def process_markdown_simple(content):
    """
    Simple processing - remove all newlines
    """
    # Remove all newlines and join with spaces
    single_line = ' '.join(content.splitlines())
    
    # Clean up multiple spaces
    cleaned_content = re.sub(r'\s+', ' ', single_line).strip()
    
    return cleaned_content

def process_markdown_preserve_structure(content):
    """
    Process while preserving some markdown structure
    """
    lines = content.splitlines()
    processed_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            # Preserve headers, code blocks, and list items with slight spacing
            if line.startswith('#') or line.startswith('```'):
                processed_lines.append(f" {line} ")
            else:
                processed_lines.append(line)
    
    # Join and clean up
    single_line = ' '.join(processed_lines)
    cleaned_content = re.sub(r'\s+', ' ', single_line).strip()
    
    return cleaned_content

# Usage
process_markdown_file(r'C:\Users\rudra\Documents\coding-projects\aws-genai-llm-chatbot\prompts\hr_assistant_prompt.md', r'C:\Users\rudra\Documents\coding-projects\aws-genai-llm-chatbot\prompts\hr_assistant_prompt_singleline.txt')