import pickle

x=[1,2,"abc"]
y={"name":"json","age":25}
myfile=open("./objdata.bin",'wb')
pickle.dump(x,myfile)
pickle.dump(y,myfile)
myfile.close()
myfile=open("./objdata.bin",'rb')
myfile.seek(0)
a = myfile.read()
print(a)
myfile.seek(0)
x=pickle.load(myfile)
y=pickle.load(myfile)
print("{}:".format(x))
print("{}:".format(y))