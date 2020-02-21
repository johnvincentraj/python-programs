#Python: Function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
#own program

inpt = 8
total = 0

for i in range(inpt-1):
    i += 1
    total = total + (i ** 3)
print(total)

#-------------------------------------------------------------------------------------------------

#Python: Function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number
#example program

def sum_of_cubes(n):
  n -= 1
  total = 0
  while n > 0:
    total += n * n * n
    n -= 1
  return total
print("Sum of cubes: ",sum_of_cubes(3))
