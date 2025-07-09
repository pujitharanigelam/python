# " sum of even numbers"
# n=int(input("enter n value"))
# s=0
# for i in range(i,n+1):
#     if (i%2==0):
#         s+=1
#         print(s)


# "print fibinoci number f(n)=f(n-1)+f(n-2)"
# n=int(input())
# l=[0,1]
# a=0
# b=1
# for i in range(n-2):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c
# print(*l)



# "count of vowles"
# s=input()
# c=0
# for each in s:
#     if each in "aeiouAEIOU":
#         c+=1
# print(c)

# "string is palindrome or not"
# s=input().split()
# l="".join(s)
# v=l.lower()
# r=v[::-1]
# if v==r:
#     print(True) 
# else:
#     print(False)    




# "count the no.of words in string"
# n=input().split()
# l=len(n)
# print(l)



# "remove duplication characters in string"
# s=input()
# r=""
# for char in s:
#     if char not in r:
#         r+=char
# print(r)        


# "string or not given two strings a&b"
# a=input()
# b=input()
# if a==b:
#     print(True)
# else:
#     print(False)    


# count consonent in a string
# n=input()
# c=0
# for each in n:
#     if each.isalpha() and each not in "aeiouAEIOU":
#         c+=1
# print(c)



s=input()
x=s.lower()
c=0
for i in x:
    if i in "bcdfghjklmnpqrstvwxyz":
        c+=1
print(c)    