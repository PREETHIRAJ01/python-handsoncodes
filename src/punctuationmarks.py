string=input("enter a string")
a='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
nopunct=""
for char in string:
    if( char not in a):
        nopunct=nopunct+char
print(nopunct)