#imports
import matplotlib.pyplot as plt
import numpy as np  

#importing data
if True == True:
    pass

#fixing data
example_data = ['name' , 'namee' , 'name' , 'namee' , 'name12' , 'name' , 'name12' , 'namee']
fixed_example_data = []
for item in example_data:
    if item == 'namee': #wrong name
        loc = example_data.index(item)
        example_data.remove(example_data[loc])
        example_data.insert(loc , 'name') #fixed name
    elif item == 'name12':
        loc = example_data.index(item)
        example_data.remove(example_data[loc])
        example_data.insert(loc , 'name') #elif statements must be added for further coorections
    else:
        pass
print(example_data)

#importing list and functions
name_list = []
name_dict = {}
names = []
num = []
sort_name_dict = {}
done = []
def Rsort():
    high = 0
    for n in name_dict:
        if done.count(n) >= 1:
            continue
        if name_dict.get(n) >= high:
            high = name_dict.get(n)
            sort_name_dict[n] = name_dict.get(n)
            done.append(n)
        else:
            pass
def sort():
    for _ in name_dict:
        high = 0
        for n in name_dict:
            if done.count(n) >= 1:
                continue
            if name_dict.get(n) >= high:
                print(1)
                high = name_dict.get(n)
                sort_name_dict[n] = name_dict.get(n)
                done.append(n)
            else:
                pass        

for name in name_list:
    n = name_list.count(name)
    name_dict[name] = n
print(name_dict)
sort()
print("sort:")
print(sort_name_dict)

for element in sort_name_dict:
    names.append(element)
    num.append(name_dict.get(element))
print(names)
print(num)

#maths and plotting:
fig = plt.figure()
ax = plt.axes()
#plt.grid()
x = names
y = num
print(x,y)
plt.xlabel('Name')
plt.ylabel('Occurences')
i = 1
constant = 5
p = []
for _ in range(100):
    p.append(constant * (1/i))
    i+=1     
plt.bar(x,y, color = 'lime')    
plt.plot(p , color = 'black')
plt.show()