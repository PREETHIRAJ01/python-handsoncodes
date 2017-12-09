s1=input("enter a string")
l=len(s1)
count=0
for i in range(0,l,+1):
    if(s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u' ):
        print(s1[i])
        count=count+1

print(count)



#for i in string
