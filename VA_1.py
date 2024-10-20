"""
Solutions to module VA 1
Student: 
Mail:
"""

def exchange(a, coins) -> list: 
    """ Count possible way to exchange a with the coins in coins. Use memoization"""
    if a == 0:
        return 1
    elif a < 0:
        return 0
    elif len(coins) == 0:
        return 0
    
    
    return exchange(a, coins[1:]) + exchange(a - coins[0], coins)


def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if not l1:
        return l2
    elif not l2:
        return l1

    return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])





def main():
    print('\nCode that demonstates my implementations\n')
    #print(exchange(5, [1, 2, 3]))
    l1 = ['a', 'b', 'c']
    l2 =  [2, 4, 6, 'x', 10]
    print(zippa(l1, l2))

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 

What happens if you try to calculate e.g. 10000?
  
"""
