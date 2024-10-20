""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):          #   
        f = self.first # Assigns the first value to f
        len = 0 
        while f: # While there are elements in f
            len += 1 
            f = f.succ # advance to the next element
        return len 


    def mean(self):               
        f = self.first # Assigns the first value to f
        sum = 0
        while f:
            sum += f.data # add the data of the element to sum
            f = f.succ # advance to the next element
        return sum / self.length() # returns the sum divided by the length using the length function.


    def remove_last(self):       # 
        f = self.first # Assigns the first value to f
        if f == None: # If there are no elements in f
            raise ValueError('Empty list') # Raise ValueError
        elif f.succ is None: # If there is no element after the current element
            temp = f.data # Store the data of the current element in a temp variable
            self.first = None # Remove the data of the current element 
            return temp # Return the value of the removed element 

        current = f # Create a new variable and give it the value of f, this is done to not alter the reference to the original first element
        while current.succ.succ: # While there is two element after current.
            current = current.succ # advance to the next element 

        temp = current.succ.data # Store the data of the last element in the list
        current.succ = None # Remove the last element 
        return temp # Return the removed value
             


    def remove(self, x):         # 
        f = self.first # Assigns the first value to f

        if f is None: # If there is no elements in the linked list
            return False 
        
        if f.data == x: # If the data of the first element contains the value to remove
            self.first = f.succ # Move the pointer to the next element in the linked list, this removes the first element
            return True
        
        current = f # Creating a new variable with the contents of f
        while current.succ is not None: # While there is still a value after current
            if current.succ.data == x: # If the value after current is equal to the value to remove
                current.succ = current.succ.succ # Move the pointer to the value after 
                return True 
            current = current.succ # Advance to the next element
        return False



    def to_list(self):            #
        def _to_list(f): # Creates an auxiliary function with the input f, f represent the current node  
            if f is None: # If f is empty
                return [] # Return an empty list
            return [f.data] + _to_list(f.succ) # Return the data of the first element in a list and run the function again on the successor
        return _to_list(self.first) # Runs the auxiliary function with the first element in the linked list

    def remove_all(self, x): 
        def _remove_all(f, x): # Creates an auxiliary function with inputs f and the value to remove
            if f is None: # Base case 
                return None, 0 
            
            new_first, count = _remove_all(f.succ, x) # Runs the auxiliary function again with the successor of the current element
            
            if f.data == x: # If the value of f is the value to remove 
                return new_first, count + 1 # Returns new_first and the updated count, this removes the examined node
            else:
                f.succ = new_first # Updating the pointer to the updated list after nodes have been removed
                return f, count # Returns the updated linked list and the count
            
        self.first, removed_count = _remove_all(self.first, x) # Call the auxiliary function
        return removed_count # 
                

    def __str__(self):            #
        return '(' + ', '.join(str(data) for data in self.__iter__()) + ')' # Joining a string of each element in the iterator between parenthesis 

    def copy(self):               #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        O(n^2): O(n) due to the for loop and O(n) for the insert function that uses a while loop.

    '''

    def copy(self):               # Should be more efficient
        result = LinkedList() # Create an empty linked list
        current = self.first # Set the current variable to the first element in the original linked list
        tail = None # Creates a variable that keeps track of the last node in the new list, initially None since there are no elements yet

        while current: # While current is a node with values.
            new_node = self.Node(current.data, None) # Create a new node with the data from the original node
            if tail is None: # If there is no tail, meaning that this is the first element in the new list
                result.first = new_node # Add the value of the new node to the results list
            else: # If there already is a node in the list 
                tail.succ = new_node # Adding the new node to the end of the list 
            tail = new_node # The tail is updated to point to the new node
            current = current.succ # Moves the pointer to the next node in the original list 
        return result 
    ''' Complexity for this implementation:
        O(n) due to the while-loop, everything else is constant time, O(1)
    '''

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:

    # Method length
    print('\nMethod length')
    print(lst.length())
    ##############

    #### Method mean ####
    print('\nMethod mean')
    print(lst.mean())

    #####################


    # Method remove last
    print('\nMethod remove last')
    #lst = LinkedList()
    #for x in [3, 1, 2]:
    #    lst.insert(x)
    
    #lst.print()
#
    #try:
    #    lst.remove_last()
    #    lst.print()
    #    lst.remove_last()
    #    lst.print()
    #    lst.remove_last()
    #    lst.print()
    #    lst.remove_last()
    #    lst.print()
    #except ValueError as ve:
    #    print('*** ValueError:', ve)
    
    ####################

    #### Method remove ####

    #lst = LinkedList()
    #for x in [3, 1, 2, 6, 1]:
    #    lst.insert(x)
    #lst.print()
    #lst.remove(2)
    #lst.print()
    #lst.remove(1)
    #lst.print()
    #lst.remove(6)
    #lst.print()
    #lst.remove(10)
    #lst.print()

    #######################

    #### Method to_list ####

    #lst = LinkedList()
    #print(lst.to_list())
    #for x in [1,4,6,2]:
    #    lst.insert(x)
#
    #print(lst.to_list())

    ########################

    #### Method remove all ####
    #lst = LinkedList()
    #for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
    #    lst.insert(x)
    #lst.print()
#
    #print(lst.remove_all(1))
    #lst.print()
    #print(lst.remove_all(9))
    #lst.print()
    #print(lst.remove_all(3))
    #lst.print()

    ### Method __str__ ###

    #print('Using the __str__ function: ')
    #print(lst.__str__())
    


if __name__ == '__main__':
    main()
