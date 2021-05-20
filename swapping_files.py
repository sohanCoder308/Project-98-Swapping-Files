# Creating a SwipeFileData Function
# Names of text files are --> file1.txt and file2.txt
def swipeFileData():
    # Taking names of the files from user and storing them
    file1_input = input("Enter name of File1:- ")
    file2_input = input("Enter name of File2:- ")

    # Opening file 1 in read mode and storing its data
    with open(file1_input, "r") as a:
        fileData_1 = a.read()

    # Opening file 2 in read mode and storing its data
    with open(file2_input, "r") as b:
        fileData_2 = b.read()  

    # Opening file 1 in write mode and writing data of file 2 in it
    with open(file1_input, "w") as a1:
        a1.write(fileData_2)

    # Opening file 2 in write mode and writing data of file 1 in it
    with open(file2_input, "w") as a2:
        a2.write(fileData_1)  

    print("Swapped the files successfully! :)")    

# Calling the function!  :)
swipeFileData()          