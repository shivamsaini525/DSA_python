def Stringrev(str):
    str1=''

    for i in str:
        str1=i+str1
    return str1
str=input("Enter the String")
rev=Stringrev(str)
print("original string",str)
print("rev string",rev )    