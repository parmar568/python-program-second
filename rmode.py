def read_file_header():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as file:
            header = file.readline().strip()
            print("File Header:", header)
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

read_file_header()