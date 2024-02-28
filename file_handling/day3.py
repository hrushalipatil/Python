
# copy image file to new file
f1=open("img.png","rb")
f2=open("new.png","wb")

bytes = f1.read()
f2.write(bytes)
f2.close()
f1.close()

# open with file -----we dont need to close this file it will close automatically

with open("mytext5.txt","r") as file:
    str = file.read()
    print(str)

with open("mytext6.txt","w") as file:
    str = input("Enter the sentence " + '\n')
    file.write(str)




