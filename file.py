'''
Symmetric Relation of Fibonacci and Lucas Number Sequences
'''

import math


def f_and_l_of_n(n):  
    # f(n) is the nth Fibonacci number, l(n) the nth Lucas number
    
    # φ, the golden ratio
    phi = (1 + math.sqrt(5)) / 2 
    
    # symmetric relation for integer argument n
    Fibonacci_number = int((pow(phi, n) - pow(1 - phi, n)) / (phi - (1 - phi)))
    Lucas_number     = int((pow(phi, n) + pow(1 - phi, n)) / (phi + (1 - phi)))
    
    return Fibonacci_number, Lucas_number
    
    
def main():
    while (True):
        length = input("Enter Fibonacci and Lucas number sequence length: ")
        
        index = 0
        
        Fibonacci_numbers = []
        Lucas_numbers = []
        
        while (index < int(length)):
            Fibonacci_number, Lucas_number = f_and_l_of_n(index)
            Fibonacci_numbers.append(str(Fibonacci_number))
            Lucas_numbers.append(str(Lucas_number))
            index += 1
            
        Fibonacci_numbers = ' '.join(Fibonacci_numbers)
        Lucas_numbers = ' '.join(Lucas_numbers)
            
        print()
        
        print("Here are the first " + length + " Fibonacci numbers: ")
        print(Fibonacci_numbers)

        print()
        
        print("Here are the first " + length + " Lucas numbers: ")
        print(Lucas_numbers)

        print("\n⋄⋄⋄\n")


main()
