#Use generator functions to create your own version of range function 
#call it my_range

def my_range(first_number, last_number):
	x = first_number
	while x < last_number:
		yield x
		x=x + 1
for i in my_range(5,10):
	print(i)



#%%
#bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..)
#have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears,
#because they each have a raised foot. 
#Recursively return the number of "ears" in the bunny line 1, 2, ... n 
#(without loops or multiplication). 


def my_function(bunnies):
 if bunnies == 0: 
    return bunnies
 return my_function(bunnies - 1) + 3 - (bunnies % 2)
print("Number of ears for bunnies" )
print(my_function(0))
print(my_function(1))
print(my_function(2))
