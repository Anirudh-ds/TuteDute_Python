
try:
    with open('output.txt', 'a') as file1:
        print("Enter data to write in file : ", end="")
        str1 = input()

        writen_data = file1.write(str1 + '\n')
        if(writen_data >= 0):
            print("Data entered successfully.")
        else:
            print("No data entered")
        print("Enter additional data to write in file : ", end="")
        str2 = input()

        writen_data1 = file1.write(str2 + '\n')
        if (writen_data1 >= 0):
            print("Data entered successfully.")
        else:
            print("No data entered")

    with open('output.txt', 'r') as file1:
        data = file1.read()
        print(data)

except FileNotFoundError:
    print("File does not exists.")
