
teks = "\nRidho Mauliddani"

with open ("C:/Users/hp/.vscode/pbo 3/pertemuan pbo ke 4/test.txt", "a") as file1:
    file1.write(teks)

file1.close()

with open("C:/Users/hp/.vscode/pbo 3/pertemuan pbo ke 4/test.txt", "r") as file2:
    read_content = file2.read()
    print(read_content)

file2.close()