#list is mutable as it can expand or 
l = [1, 2, 4]
#tuples is immutable therefore you cant change it as in you can add more items to it 
#but if the item in it is mutable then it can be changed
l = (1, 2, 4)

str = 'thisdamnstring'

print(l[0])

for chr in str:
    print(chr)


#set are iterable but it is not a sequence therefor you cant get an item using indexing and if 
#iterate through it, it is not guarantee that each item will be printed in order

set = {1,2,"n",3,"4",5}

for num in set:
    print(num)