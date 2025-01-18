# dict={
#     "brand":"maruti",
#     "year":"2024",
#     "name":"Toyato",
# }
# dict["year"]=2025
# print(dict)


# list=["Apple", "Banana", "Grapes", "Mango"]
# list1=["Tomato","Carrot"]
# # print(list)
# # list.append("Kiwi")
# # list.insert(3,"orange")
# list.extend(list1)
# print(list)


n=int(input("Enter a number: "))
x=n
rev=0
while x>0:
    r=x%10
    rev=rev*10+r
    x=x//10
if rev==n:
    print(n,"is a palindrome")
else:
    print(n,"is a not palindrome")