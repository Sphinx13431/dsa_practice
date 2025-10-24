'''
Stack of Plates: Imagine a (literal) stack of plates. 
If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack 
exceeds some threshold. Implement a data structure SetOfStacks that mimics this. 
SetO-fStacks should be composed of several stacks and should create a new stack once 
the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should 
behave identically to a single stack (that is, pop () should return the same values as 
it would if there were just a single stack).
'''

class SetOfStacks:
    def __init__(self, capacity: int):
        self.stacks = []          # list of substacks
        self.capacity = capacity  # max plates per stack
        
    def push(self, value: int):
        # if no stacks yet, create one
        if len(self.stacks) == 0:
            self.stacks.append([])

        # if the last stack reached capacity, make a new one
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

        # push value into the last stack
        self.stacks[-1].append(value)

    def pop(self) -> int:
        # if all stacks empty
        if len(self.stacks) == 0:
            return -1

        # pop from last stack
        ele = self.stacks[-1].pop()

        # if that stack is empty, remove it
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return ele
    
    def pop_at_index(self,index:int)->int:
        if index < 0 or index >= len(self.stacks):
            print("Invalid stack index")
            return -1

        ele = self.stacks[index].pop()

        # if that stack is empty, remove it
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        return ele
