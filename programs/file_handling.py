import os

file_path = r"C:\Users\rudra\Documents\coding-projects\aws-genai-llm-chatbot\files\malware_introduction.txt"
filename = os.path.basename(file_path)

print("Opening file", filename, "for reading.")
file = open(file_path, "r")

print("File opened successfully. Reading contents:")
# Read and print the file contents line by line
for line in file:
    print(line, end='')

file.close()
print("\nFile closed.")