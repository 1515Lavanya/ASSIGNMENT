# dict = {
#     "name" : "lavanya hema",
#     "subjects" : {
#         "phy" : 40,
#         "chem" : 50,
#         "bio" : 40,
#         "math" : 60,
#         "topics" : ("html","java","css"),
#         "pairs" : ["java","klak","hgff"]
#     }
# }

# print(dict.get("name"))
# STES
# collection = {1,2,3,4,5,6,0,7,"True","hello",7,7,7}
# print(collection)
# print(len(collection))
# collection = set()

# print(type(collection))
# collection = set()
# # collection.add(2)
# collection.add(3)
# collection.add(2)
# collection.add("apnacollage")
# collection.add((1,2,3))
# # collection.add([1,2,3])
# # collection.remove(7)


# collection.clear()
# print(len(collection))
# collection = {"hello","skywaves","world"}
# print(collection.pop())
# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.intersection(set2))
# print(set1)
# print(set2)
# subjects = {
#     "python","java","c++" , "python", "javascript","java","python",
#     "java","c++","c"
# }
# print(len(subjects))

# marks ={}


# x = int(input("enter phy : "))
# marks.update({"phy" : x})

# x = int(input("enter math : "))
# marks.update({"math" : x})

# x = int(input("enter eng : "))
# marks.update({"bio" : x})


# values = {
#     ("float" , 9.0),
#     ("int" , 9)
# }
# count = 1
# while count <=5:
#     print("hello")
#     count +=1
# print(count)

# i = 1
# while i <= 5 :
#     print("abhu",i)
#     i+=1
# print(i)
#  print no.s 1 from 1 to 5
# i = 1
# while i <=5:
#     print(i)
#     i+=1
# print("loop ended")

# i = 5
# while i >=1:
#     print(i)
#     i = i-1
# print("loop ended")
# i = 1
# while i<=100:
#     print(i)
#     i = i+1
# print("end loop")

# i = 100
# while i >=1:
#     print(i)
#     i = i-1
# n = int(input("enter number :"))
# i = 1
# while i<=10:
#     print(n*i)
#     i = i+1
# nums = [1,4,9,16,25,36,49,64,81,100]
# heroes = ["batman","spiderman","hanuman"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx=idx+1
# nums = (1,4,9,16,25,36,49,64,81,100)
# i = 1
# while i <=5:
#     print(i)
#     if(i==3):
#         break
#     i = i+1

# print("end of loop")
# x = 36
# i = 0 
# while i < len(nums):
#     print(nums(i))
#     i = i+1

# count = 1
# while count <= 5:
#     print("hello")
#     count = count + 1
 
# print(count)

# i = 1
# while i<=5:
#     print(i)
#     i = i+1
# # i = 1
# while i<=5:
#     print(i)
#     i = i+1
# i = 5
# while i >= 1:
#     print(i)
#     i = i -1
# i = 5
# while i>=1:
#     print(i)
#     i = i - 1
# i = 1
# while i <=10:
#     print(8*i)
#     i = i +1

# nums = [1,4,9,16,25,36,49,64,81,100] 
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx = idx +1
# print "hello" five times
# i = 1
# while i <=5:
#     print("hello")
#     i = i+1

# # print "abhu i love u " 10 times
# i = 1
# while i <= 10:
#     print("i love u abhu")
#     i = i +1
# print(i)

# # print numbers 5 to 1
# i = 5
# while i >=1:
#     print(i)
#     i = i - 1
# print(i)

# # wap to print number from 1 to 100
# i = 1
# while i <=100:
#     print(i)
#     i = i +1
# print(i)

# # wap to print number from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i = i-1
# # wap to print numbers from 1 - 100
# i = 1 
# while i >=100:
#     print(i)
#     i = i+1
# i = 100
# while i <= 1:
#     print(i)
#     i = i - 1

# n = int(input("enter number:"))

# i = 1
# while i <=10:
#     print(n*i)
#     i = i+1

# num = [1,4,9,16,25,36,49,64,81,100]
# idx= 0 
# while idx < len(num):
#     print(num[idx])
#     idx = idx+1
# nums = (1,4,9,16,25,36,49,64,81,100)
# i = 0

# x = 36

# i = 0
# while i < len(nums):

# light =  "yellow"

# if(light == "red"):
#     print("stop")
# if(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("broken")

# print('end of code')
# num = 6
# if (num>8):
#     print("greater than 8")
# elif (num >3):
#     print("greater than 3")
# age = 14
# if(age >= 18):
#     print("can vote")
# else:
#     print("cannot vote")
# marks = int(input("enter your marks:"))
# if (marks >= 90):
#     grade = "A"
# elif(marks >=80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks <80):
#     grade = "C"
# else :
#     grade = "D"

# print("grade of the student - >", grade)
# nesting
# age = 82
# if(age >= 18):
#     if(age>=80):
#         print("cannot drive")
#     else:
#         print("cann drive")
# else :
#     print("cannot drive")
# num = 14
# rem = num % 2 
# if(rem == 0):
#     print("even")
# else:
#     print("odd")
x = int(input("enter a number:"))
if (x %7 == 0):
    print("multiple of 7")
else :
    print("not a multiple")





 









  





  