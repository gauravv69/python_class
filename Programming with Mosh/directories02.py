from pathlib import Path

# This method will seacrh all the py files in the current directory 
path = Path()
for file in path.glob('*.py'):
    print(file)