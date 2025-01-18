# LIST:-
# List are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store 
# collections of data, the other 3 are Tuple, Set, and Dictionary, 
# all with different qualities and usage.

# Lists are created using square brackets:

# Eg:-
# Create a List:-

# list=["apple","banana","mango","grapes"]
# print(list[0])


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[0])

# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(len(list1))

# list1=["apple","banana","grapes"]
# list2=[1,34,56,83]
# list3=[True, False,True,True]

# print(list1)
# print(list2)
# print(list3)

# list1=["apple","banana","grapes"]
# print(type(list1))

# list1=list(("apple","banana","grapes"))
# print(list1)


# Example:-

# A list with strings, integers and boolean values:-

# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

#-------------------------------------------------------------------------

#Acess list item:-Ranges of indexes[0],[1],[-1]

# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[1])


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[-3:-1])
# o/p:-['cherry', 'apple']


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[-2])
# o/p:-['cherry', 'apple']


# list1 = ["apple", "banana", "cherry", "apple", "grapes"]
# print(list1[1:4])
# o/p:-['banana', 'cherry', 'apple']


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[:3])
# o/p:-['apple', 'banana', 'cherry']


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[2:])
# o/p:-['cherry', 'apple', 'cherry']


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# print(list1[-4:-1])
# o/p:-['banana', 'cherry', 'apple']


# list1 = ["apple", "banana", "cherry", "apple", "cherry"]
# if "cherry" in list1:
#     print("yes,'cherry' in the list")
# else:
#     print("no,'cherry is not in a list")


# list=["apple","grapes","banana","orange","mango"]
# if "orange" in list:
#      print("yes",'mango is in the list')
# else:
#      print("no",'mango is not in the list')
#o/p:-yes mango is in the list


# list=["apple","grapes","banana","orange","mango"]
# if "kiwi" in list:
#      print("yes",'kiwi is in the list')
# else:
#      print("no",'kiwi is not in the list')
#o/p:-no kiwi is not in the list

#-----------------------------------------------------------

#change list items:-

# list=["apple","banana","cherry"]
# list[1]=["grapes"]
# print(list)
# o/p:-['apple', 'grapes', 'cherry']


# list1=["apple","banana","mango","grapes"]
# list1[1:3]=["Nithya","malleswar"]
# print(list1)
#o/p:-['apple', 'Nithya', 'malleswar', 'grapes']


# list=["mango","apple","banana"]
# list[0]="grapes"
# print(list)
# o/p:-['grapes', 'apple', 'banana']


#------------------------------------------------------

#Add list items:-Append,Insert,Extend

# list=["apple","banana","cherry"]
# list.append("orange")
# print(list)

# list1=["apple","banana","cherry"]
# list1.insert(2,"grapes")
# print(list1)
# o/p:-['apple', 'banana', 'grapes', 'cherry']

# list1=["apple",'grapes',"banana"]
# list1.insert(1,"kiwi")
# print(list1)
# o/p:-['apple', 'kiwi', 'grapes', 'banana']


# list1=["apple","banana","cherry"]
# list2=["grapes","kiwi","orange"]
# list1.extend(list2)
# print(list1)

     #(or)
     
# list1=["apple","banana","grapes","cherry"]
# list2=["mango","kiwi"]
# list1.extend(list2)
# print(list1)
#o/p:-['apple', 'banana', 'grapes', 'cherry', 'mango', 'kiwi']

#--------------------------------------------------

#Remove list items:-Remove,Pop,del,Clear

# list1=["apple","banana","cherry"]
# list1.remove("banana")
# print(list1)
# o/p:-['apple', 'cherry']

# list1=["apple","banana","cherry","grapes"]
# list1.pop(2)
# print(list1)
#o/p:-['apple', 'banana', 'grapes']

# list1=["apple","banana","cherry","grapes"]
# del list1[0]
# print(list1)
#o/p:-['banana', 'cherry', 'grapes']

# list1=["apple","banana","cherry","grapes"]
# list1.clear()
# print(list1)
# o/p:-[]

#-----------------------------------------------------

#sort list

# list=["grapes","mango","apple","banana"]
# list.sort()
# print(list)
# o/p:-['apple', 'banana', 'grapes', 'mango']

# list=[8,5,3,10,6,2,1]
# list.sort()
# print(list)
# o/p:-[1, 2, 3, 5, 6, 8, 10]


# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)
# o/p:-[100, 82, 65, 50, 23]

#---------------------------------------------------------


#Join list

# a=["apple","banana","cherry"]
# b=[1,2,3,4,5]
# c=a+b
# print(c)
# o/p:-['apple', 'banana', 'cherry', 1, 2, 3, 4, 5]

# list1=["apple","mango"]
# list2=[5,10]
# list3=list1+list2
# print(list3)
# o/p:-['apple', 'mango', 5, 10]