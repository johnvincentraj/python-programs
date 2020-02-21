#Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values
#own program

dt2 = [2,4,6,8]
flag = False

for i in dt2:            
        for j in dt2:
            if(i != j):
                k = i * j
                if(k % 2 != 0):
                    flag = True
                else:
                    pass
                
if(flag):
    print(True)
else:
    print(False)
                    
#________________________________________________________________________________________________________________________

#Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values
#example program

def odd_product(nums):
  for i in range(len(nums)):    
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        print(product)
        if 1 & 1:
          return True
        return False
          
dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]

print(dt1, odd_product(dt1));
