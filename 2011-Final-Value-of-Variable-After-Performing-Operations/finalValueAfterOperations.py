class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        count = 0
        for i in range (len(operations)):
            if operations[i]=="--X" or operations[i]=="X--":
                count-=1
            elif operations[i]=="X++" or operations[i]=="++X":
                count+=1
        return count