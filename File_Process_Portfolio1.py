try:
    with open("test_file_Portfolio1.txt","r") as file:
        for line in file:
            content = file.read()
            file.seek(0)
            content2 = file.read()
            print(content)
            print(content2+"content2")
except FileNotFoundError:
    print("⚠️ Error: The file 'test_file_Portfolio.log' is missing! Please check the name.")

    file.close()

