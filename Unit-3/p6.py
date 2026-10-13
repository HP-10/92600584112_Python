import os
import sys

print("=== File and Directory Operations ===")

print("Current Directory:", os.getcwd())

os.mkdir("Test")
print("Directory Created - 'Test'")

file = open("Test/demo.txt", "w")
file.write("Hello Python")
file.close()

print("File Created - 'demo.txt'")
print("Files:", os.listdir("Test"))

os.remove("Test/demo.txt")
os.rmdir("Test")

print("File and Directory Deleted - 'Test/demo.txt'")
print("Python Version:", sys.version)