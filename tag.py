import csv
from pathlib import Path
try:
    file = input("Enter the name of the file: ")
    file_path = Path(file)
    
    if file_path.suffix != ".csv":
        raise TypeError("Only csv files are allowed!")
    
    with open(file, "r") as f:
        read = csv.reader(f)

        for row in read:
            print(row)

except TypeError as e:
    print(e)

except FileNotFoundError:
    print(f"The file doesen't exist :D")