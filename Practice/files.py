from pathlib import Path

path = Path("Practice")
print(path.exists())

path1 = Path("eccommerce")
print(path1.mkdir()) #create directory
print(path1.rmdir()) #remove directory

dir = Path()
for files in dir.glob("*.*"):
    print(files)
