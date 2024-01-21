# to-read-file
# file1 = open('test.txt', 'r')
# print(file1.read())
#
# # to-read-5-letters-from-file
# file1 = open('test.txt', 'r')
# print(file1.read(5))
#
# # to-readline
# file1 = open('test.txt', 'r')
# print(file1.readline())
#
# # to-read-2-lines
# file1 = open('test.txt', 'r')
# print(file1.readline())
# print(file1.readline())

# loop-through-file
# for x in file1:
#     print(x)

# close-file
# print(file1.readline())
# file1.close()

# append-file
# file1 = open("test.txt", 'a')
# file1.write("Now the file has more content!")
# file1.close()
#
# file1= open("test.txt", 'r')
# print(file1.read())

# append-file-to-new-line
# file1 = open("test.txt", 'a')
# file1.write("\nNow the file has more content!")
# file1.close()
#
# file1= open("test.txt", 'r')
# print(file1.read())

# overwrite-to-existing-file-using-new-content
# file1 = open("test.txt", 'w')
# file1.write("New Content")
# file1.close()
#
# file1 = open("test.txt", 'r')
# print(file1.read())

#to-create-newfile-using-'a'-if-there-is-no-existing-file
# file2 = open("test1.txt","a")

#to-create-newfile-using-'x'-if-there-is-no-existing-file-and-return-error-if-file-exist
# file2=open("test2.txt", "x")

#Create a new file if it does not exist using 'w'
# f = open("myfile.txt", "w")


#delete-a-file
# import os
# os.remove("test1.txt")

#check-if-file-exists-and-then-delete
# import os
# if os.path.exists("test1.txt"):
#     os.remove("test1.txt")
# else:
#     print("The file does not exist")