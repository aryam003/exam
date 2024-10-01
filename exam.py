'''Q-17'''

'''file creation'''
# e=open('exam/t.txt','x')
# e.write('python exam demo file')

p=open('exam/t.txt','r')
a=len(p.readlines())
p.seek(0)
longest_w=''

# # print(a)
# for i in a:
#     if len(i)>len(longest_w):
#         longest_w=i
# print(longest_w)
'''longest line'''

# for i in range(a):
#     f=p.readline().strip()  
#     h=f.split(' ') 
#     for j in h:
#         if j!='':
#             if len(longest_w)<len(j):
#                 longest_w=j
# print('longest_w:',longest_w)

#longest word 
'''longest word:'''


'''Q-12'''
# l=[1,2,3,4,4,5]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

'''Q-14'''
# for i in range(1,5):
#     a=64
#     for b in range(i):
#         print(chr(a+i-b),end=' ')
#     print()

''' A 
    B A 
    C B A 
    D C B A '''

'''Q-15'''
# def f():
#     a=int(input("enter a value:"))
#     i=1
#     factorial=1
#     while i<=a:
#         factorial*=i
#         i+=1
#     print(factorial)
# f()   
def f():
    a=int(input("enter a value:"))
    factorial=1
    for i in range(1,a+1):
        factorial*=i
    print(factorial)
f()


'''factorial of a number'''

'''Q-16'''
# d={1:'one',2:'two',3:'three'}

# def num(d):
#     # d1={}
#     # for i in d:
#     #     d1[d[i]]=i
#     # return d1
#     return {value:key for key,value in d.items()}
# print(num(d))
'''value:key for key,value in d.items
   ----------------------------------
   for i,j in d.items():
      print({i,j})
    'i=key , j= value 
    for key,value in d.items '''



