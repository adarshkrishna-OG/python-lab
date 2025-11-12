file=open("files 2.txt","w")
file.write("hello world!\n welcome to python programming\nThank you")
file.close()
list=[]
file=open("files 2.txt", "r")
list=[line.strip() for line in file]
file.close()
print(list)