# Inventory Management Program

print ('=====Inventory Management=====')

# Input number records
x = int(input('How many Records to be created : '))

j = (' ')
k = (' ')
h = (' ')
u = (' ')

# Entering Items, Code and Cost
while True:
        for i in range(x):
                y = input('Enter Item Name : ')
                g = int(input('Enter Code : '))
                p = int(input('Enter Cost : '))
        j = j + (' ') + y + (' ') + str(g) + (' ') + str(p)
        k = k + (' ') + y 
        h = h + (' ') + str(g)
        u = u + (' ') + str(p)

# Working on this one
def Final_Item():
        print ('Item/Items : ') + print(k)
def Final_Code():
        print ('Code : ') + str(h)
def Final_Cost():
        print ('Cost : ') + str(u)
print('           ')

print ('---Stock Information---')

print('            ')

# Printing final product displays (working on this one)

Final_Item()
Final_Code()
Final_Cost()

print('            ')

b = input('Would you like to save? ')
if b == ('yes'):
        print('Saved')
else:
        print('Items have been discarded.')
        print('Quit program and press run to start over')








