#string1=input("please enter a string")
#l=len(string1)
#for i in range(0,l):
# if(string1[i]!=string1[l-i-1]):
#flag=1
    #break
#if flag==1:
    #print("not a palindrome")
#else:
#    print("palindrome")

str= input("enter a string")
str= str.casefold()
rev_str = reversed(str)
if list(str) == list(rev_str):
    print("It is palindrome")
else:
    print("It is not palindrome")



