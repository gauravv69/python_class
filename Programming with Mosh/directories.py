from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft

# Relative path: which includes directory we have in our project i.e. ecommerce

# This method checks whether the path exists. 
path = Path("ecommerce")
print(path.exists())

# This method creates a new path
path = Path("emails")
print(path.mkdir())

# This method removes the path
path = Path("emails")
print(path.rmdir())