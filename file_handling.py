"""# step 1: create and write to a file
with open("jattends.txt","w") as file:
    file.write("Hello , this is jattends file.\n")
    file.close()

# step 2: read the content of the file
with open("jattends.txt","r")as file:
    print(file.read())"""

"""# step 3 : read image
with open("python.jpg",'rb')as file:
    content = file.read()
with open("python5.jpg",'wb')as file:
    file.write(content)"""

# topic 1 : pickling
import pickle
data = {"Name" : "nithanth","course" : "python" , "age" : 25}

with open("data.pkl","wb") as file:
    pickel = pickle.dumps(data,file)

