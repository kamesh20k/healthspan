# Function to print binary number using recursion
def convertToBinary(n):
   if n > 3:
       convertToBinary(n//2)
   print(n % 4,end = '')

# decimal number
dec = 35

convertToBinary(dec)
print()

