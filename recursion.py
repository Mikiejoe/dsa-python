import math
def factorial(n):
    if n == 0:
        return 1
    else:
        f = n*factorial(n-1)
    return f

# print(factorial(4))


def bitStr(n:int,s:str)->list:
    """_summary_

    Args:
        n (int): the length of the permutated list
        s (str): the string to be permutated

    Returns:
        list: a list of all possible permutations of s of length n
    """
    if n == 1:
        return s
    return [ digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]

# print(bitStr(3,'abce'))

def karatsuba(x:int,y:int)->int:
    #the base case for recursion
    if x < 10 or y<10:
        return x*y
    
    #sets n,, the number of digits in the highest input number
    n = max(int(math.log10(x)+1),int(math.log10(y)+1))
    print('n= ',n)
    
    #rounds up n/2
    n_2 = int(math.ceil(n/2))
    print("n_2=",n_2)
    
    #adds 1 if n is odd
    n = n if n%2 == 0 else n+1
    print('n= ',n)
    
    #splits the input numbers
    a,b= divmod(x,10**n_2)
    c,d= divmod(y,10**n_2)
    print('a= ',a," b= ",b,'c= ',c," d= ",d)
    
    #applies the recursive steps
    ac = karatsuba(a,b)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d)) - ac - bd
    
    #performs the multiplications
    return (((10**n)*ac)+bd+((10**n_2)*(ad_bc)))

print(karatsuba(111,111))
    
    