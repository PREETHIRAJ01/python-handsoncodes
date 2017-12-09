bill_id=input("please enter billno")
cus_id=input("please enter cus id")
bill_amount=input("please enter bill amount")
cus_name=input("please enter cus name")
if(len(cus_name)>=3) and (len(cus_name)<=20) is True:
    print("bill_id",bill_id)
    print("cus_id",cus_id)
    print("bill_amount=rs.",bill_amount)
    print("cus_name",cus_name)
else:
    print("inavalid customer name ,cusname must be between 3 and 20");
    
    
