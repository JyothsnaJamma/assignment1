from urllib.request import urlopen

#link = "https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html"

link=input("enter the url:")

f = urlopen(link)
myfile = f.readlines()
print(myfile)