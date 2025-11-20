        #list
# l=[10,"garba",23.34,True]

# for i in l:
#     print(i)

# l=[]
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])

# l[1]="dandiya" #change value
# print(l)
# l[3]="false"
# print(l)

# for i in range(len(l)):
#     print(l[i])

# l=[10,20,30,40,50]     list slicing
# print(l[-1:-3:-1])

#list methods

# append
# extend
# insert
# pop
# del
# remove

# l=[12,12,34,56,78,98]
# for i in range(len(l)):
#     print(l[i])

# method 1 append

# l=[10,20,30]
# # l.append(40) #add number
# # l.insert(1,50) #index add number

# print(l)


# l1=[10,20,30,40]
# l2=[50,60,70]
# l1.extend(l2)  #two list add number
# print(l1)

# l=[-10,12,45,-18,-1,4,5]
# pos=[]
# neg=[]
# for i in l:
#     if i<0:
#       neg.append(i)
#     else:
#      pos.append(i)

# print(pos)
# print(neg)


# l=[10,20,30,40]
# l.pop(1)  #delete number
# l.remove(10) #perticular number delete
# l.clear() #clear number
# del(l)
# print(l)

# l=[2,7,10,14,20]
# target=9
# for i in range(len(l)):
#     if l[i]+l[i+1] == target:
#         print(l[i],l[i+1])
#         break

#deep copy

# a=[10,20,30,40,50]
# b=a
# b[0]=100
# print(a)

#shallo copy

# a=[10,20,30,40,50]
# b=a.copy()
# b[0]=100
# print(a)


# size=int(input("enter size of list:-"))
# l=[]
# for i in range(size):
#     a=int(input("enter element:-"))
#     l.append(a)
# print(l)


# l=[1,2,3,4,5]
# # print(l[::-1])    #first method
# l2=[]
# for i in range(len(l)-1,-1,-1): #second method
#     l2.append(l[i])
    
# print(l2)


# n=int(input("enter size-"))
# l=[]
# sum=0
# for i in range(n):
#     a=int(input("enter element:-"))
#     l.append(a)
#     sum=sum+a
# print(sum)

# l=[10,20,30,40,50]
# sum=0              #average  mean 
# for i in l:
#     sum=sum+i

# print(f"mean of your list is {sum/len(l)}")


#sorting , searching

# a=[12,45,23,89,45,67,89,12,86,345,23]
# search=23
# for i in range(len(a)):
#     if a[i]==search:
#         print(f"{a[i]} is at {i} index")      #searching index
#         break
# else:
#     print("sorry so such element exists")


                 ##binary search(sorted list)


# a=[1,2,3,4,5,6,7,8,9,11,12,13,14,15]
# search=3

# low=0
# high=len(a)-1
# mid=(low +high)//2

# while low <=high:
#     if a[mid]==search:
#      print(f"element found at index {mid}")
#      break
    
#     elif a[mid]>search:
#        high=mid-1
#        mid=(low+high)//2
#     elif a[mid]<search:
#        high=mid+1
#        mid=(low +high)//2

# else:
#    print("sorry so much element exist")


# def search(a,s):
#     for i in range(len(a)):
#         if a[i] ==s:
#             return f"element found at index{i}"
#     return "no such element exist"

# a=[10,20,30,40,50,60]
# print(search(a,50))
# print(search(a,30))

#######binary search


# def binary_search(a,s):
#     start=0
#     end=len(a)-1
#     mid=(start+end)//2
#     while start <=end:
#         if a[mid] ==s:
#             return f"element found at index{mid}"
#         elif a[mid]>s:
#             end=mid-1
#             mid=(start+end)//2
#         elif a[mid] <s:
#             start =mid+1
#             mid =(start+end)//2
#     return f"no search element found"
    

# a=[10,20,30,40,50,60]
# print(binary_search(a,20))


####list is sorted form
# a=[1,2,3]

# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         print("you list is not sorted")
#         break
# else:
#     print("your list is sorted")
    
                                                                           ##bubble short


# a=[12,34,56,4,5,4,34,433,45,34,44]
# for j in range(len(a)-1):          ### list line by line run
#  for i in range(len(a)-(j+1)):
#     if a[i]>a[i+1]:
#         a[i],a[i+1]= a[i+1],a[i]

# print(a)


# l=[2,96,69,77,145,34]
# max_val=l[0]
# index=0
# for i in range(len(l)-1):
#     if max_val <l[i+1]:
#         max_val=l[i+1]
#         index=i+1

# print(max_val,index)


# l=[2,96,69,77,145,34]
# max_val=l[0]
# index=0
# for i in range(len(l)-1):
#     if max_val >l[i+1]:
#         max_val=l[i+1]
#         index=i+1

# print(max_val,index)


# l=[2,96,69,77,145,34]
# max=l[0]
# smax=l[0]
# lowest=l[0]
# for i in range(len(l)):
#     if l[i]>max:
#         smax=max
#         max=l[i]

# print(lowest,max,smax)


################                                                    functions

# def add():
#     a=23
#     b=34
#     print(a+b)
# add()

# def add(a,b,c):
#     print(a+b+c)
# add(12,34,34)
# add(23,23,44)        ###  positinal parameters

# def greet():
#     print("how are you")
# def multi(a,b):
#     print(a*b)

# greet()
# multi(12,344)

##############                            return  = 1.value return  2.function break

# def add(a,b):
#     return a+b
# print("hello")
# print(add(19,23))

###############                                default prameter

# def barish(name,age,food="user"):
#     print(f"{name} {age} {food}")

# barish(20,"pizza","suprit")

############                                    recursion 

# def count(n):
#     if n ==10:
#         return
#     print(n)
#     count (n+1)

# count(1)  
 
#######################                     factorial

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(10))

























