def firstDuplicate(a):
  duplicate_list={}
  for number in a:
    if(duplicate_list.get(number)!=None):
      return number
    duplicate_list[number]= number
  return -1

a=[]
a_string = input("Please write the list, separated by a comma: ")
a = a_string.split(", ")

print(firstDuplicate(a))


#OTHER ATTEMPTS
#[2, 1, 3, 5, 3, 2]
#[3, 0, 2, 4, 6, 3, 2]
#[8, 4, 6, 2, 6, 4, 7, 9, 5, 8]

# def firstDuplicate(a):
#     visited=[]
#     for number in a:
#       #CHECKS IT IS NOT VISITED
#       if (visited.count(number)!=0):
#         return number
#       elif a.count(number)> 1:
#         visited.append(number)
#     return -1

# def firstDuplicate(a):
#   index=0
#   for number in a:
#     if int(number)<0:
#       return number*-1 
#     elif a.count(number)>1:
#       a[a.index(number, index+1)]= -int(number)
#     index+=1
#   return -1