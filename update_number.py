#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Change to the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit_and_push():
    # Stage the changes
    subprocess.run(['git', 'add', 'number.txt'], check=True)
    
    # Create commit with current date
    date = datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Update number: {date}"
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    
    # Push changes to the remote repository
    subprocess.run(['git', 'push'], check=True)

def main():
    try:
        # Read the current number from file
        current_number = read_number()
        # Increment the number
        new_number = current_number + 1
        # Write the new number back to the file
        write_number(new_number)
        # Commit and push changes to Git
        git_commit_and_push()
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()