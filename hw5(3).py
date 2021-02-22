#%%
#The program below gives elapsed execution time in seconds of the print statement 
#Create a decorator function that will take any function, 
#with any number of arguments and print the time it takes to execute it

from functools import wraps
import time

def timeit(my_func):
   @wraps(my_func)
   def timed(*args, **kw):
   
       starttime = time.time()
       output = my_func(*args, **kw)
       endtime = time.time()
       
       print('"{}" took {:.3f} ms to execute\n'.format(my_func.__name__, (endtime - starttime) * 1000))
       return output
   return timed

@timeit
def Multiply_numbers(List):
   result = 1
   for x in List:
        result = result * x
   return result
list1 = [1, 2, 4, 5, 7, 8]
print(Multiply_numbers(list1))

#%%
from functools import wraps
from time import process_time


def measure(func):
   @wraps(func)
   def _time_it(*args, **kwargs):
       start = process_time() 
       try:
           return func(*args, **kwargs)
       finally:
           end_ = process_time() - start
           print(
               f"Total execution time {func.__name__}: {end_ if end_ > 0 else 0} ms"
           )

   return _time_it
   
@measure
def sum_numbers(n):
   """Sum the numbers from 1 to n inclusive"""
   return sum([number for number in range(1, n+1)])


if __name__ == '__main__':
   n = 500
   print("The sum of the first {} numbers is: {}".format(n, sum_numbers(n)))
