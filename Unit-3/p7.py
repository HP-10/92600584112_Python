import shutil
import os

with open("./Unit_3/original.txt", "w") as file:
    file.write("Hello usnig shutil!")

shutil.copy("./Unit_3/original.txt", "./Unit_3/copied.txt")
print("File copied to 'copied.txt'")

shutil.move("./Unit_3/original.txt", "./Unit_3/moved.txt")
print("File moved and renamed to 'moved.txt'")

os.remove("./Unit_3/copied.txt")
os.remove("./Unit_3/moved.txt")
print("Files Deleted Successfully!")