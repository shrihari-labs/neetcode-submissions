class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        oneCount = 0
        zeroCount = 0
        for i in students:
            if i:
                oneCount += 1
            else:
                zeroCount += 1
        for i in sandwiches:
            if i:
                if oneCount == 0:
                    return oneCount + zeroCount
                else:
                    oneCount -= 1
            else:
                if zeroCount == 0:
                    return oneCount + zeroCount
                else:
                    zeroCount -= 1
        return 0

        
        