# touch.py
import sys
import os

def main():
    # Check if the user provided a filename
    if len(sys.argv) != 2:
        print("Usage: touch 'filename_here'")
        return

    # Get the filename from the command-line arguments
    filename = sys.argv[1]

    # Create the file if it doesn't already exist
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('')
    else:
        print(f"File '{filename}' already exists.")

if __name__ == '__main__':
    main()
