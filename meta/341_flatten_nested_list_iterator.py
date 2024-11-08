# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.int_stack = []
        nested_stack = nestedList
        self.ptr = 0
        while nested_stack:
            cur = nested_stack.pop()
            
            nested = cur.getList()
            if not nested and cur.isInteger():
                self.int_stack.append(cur.getInteger())
            else:
                for elem in nested:
                    nested_stack.append(elem)
        
        self.int_stack = self.int_stack[::-1]
    
    def next(self) -> int:
        res = self.int_stack[self.ptr]
        self.ptr += 1
        return res
        
    def hasNext(self) -> bool:
        return self.ptr < len(self.int_stack)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Have nestedList be a stack at first. Every time we pop the stack, check if the elem is a list.
# If it isn't, add it to the int stack if it's an integer
# Otherwise, add every element in that list into the nested stack
# Reverse the int stack at the end, and have a pointer iterate through it