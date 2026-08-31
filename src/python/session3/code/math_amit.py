def factorial(num : int) :
    ''' 
    calculate n! using recursion

    parameters 
    ----------
    num : int

    returns
    -------
    int
    '''
    if num < 0 :
        return ValueError("Factorial is undefiend for negative values")
    if num == 0 or num == 1 :
        return 1
    return factorial(num - 1) * num

def is_prime(num) ->bool :
    ''' 
    Chech whether a number is prime 

    paramter
    --------
    num : int

    return
    ------
    bool

    True if prime , otherwise False
    '''
    if num < 2 :
        return False
    for i in range(2, num) :
        if num % i == 0 :
            return False 
    return True

def common_divisors(num1 : int , num2 : int) -> list[int] :
    limit = min(num1, num2)
    divisors = []

    for divisor in range(1, limit + 1) :
        if num1 % divisor == 0 and num2 % divisor == 0 :
            divisors.append(divisor)
    return divisors

