 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
 
    rev = 0
    while num != 0:
 
        digit = num % 10
  
        rev = rev*10 + digit   
        num //= 10
    return rev   
if __name__ == "__main__":
    number= int(input("Enter num : "))
    res = reverse_number(number)
    print(res)
    
 
 
  