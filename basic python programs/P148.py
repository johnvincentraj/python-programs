#Python: Find the maximum and minimum numbers from a sequence of numbers
#own

inpt = [1,112,3,4,5,16,7,-9,6]


for i in (inpt):
    if(i > j):
        j = i    
    if(i != 0):
        if(i < k):
            k = i
    else:
        k = 0
        break;

    
print(j, k)
    
#----------------------------------------------------------------------------


def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
