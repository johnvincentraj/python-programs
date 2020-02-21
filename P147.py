#Python: Function to check whether a number is divisible by another number

number = 11

for i in range(2,number):
    if(number % i == 0):
        flag = True
        break
    else:
        flag = False
print(flag)
    
#------------------------------------------------------------------------------


def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))
