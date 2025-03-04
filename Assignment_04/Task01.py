
try:
    with open('sample.txt', 'r') as file1:
        data = file1.read()
        print(data)
except FileNotFoundError:
    print("File does not exists.")
