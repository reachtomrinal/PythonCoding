# file operation for reading wring and apending
# r = reading an existing file
# r+ = reading and writing the file
# a = append the file at the end
# w= writing into an existing file if the file is present otherwise write into a new file

# try:
employeeFile = open("employeeData.txt", "w")
employeeFile.write("Mrinal -  CEO")
employeeFile.close()

employeeFile = open("employeeData.txt", "a")
employeeFile.write("\nRahul -  Software Developer")
employeeFile.close()

# read a file
employeeFile = open("employeeData.txt", "r")
for employee in employeeFile:
    print(employee)

# except FileExistsError err:
# print(err)

# except:
# print("error")
