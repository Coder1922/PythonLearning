f=open("sample.txt","w")
f.write("This is a sample text file.\n")
f.write("It contains multile lines.")
f.close()

try:
    f=open("sample.txt","r")
    print("Reading file content:")
    print("Line 1:",f.readline().rstrip())
    print("Line 2:",f.readline())
    f.close()
except FileNotFoundError:
    print(f"Error: The file '{f.name}' was not found")
