class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, tem in enumerate(temperatures):
            while stack and tem > stack[-1][1]:
                stackInd, stackTem = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([i, tem])
        return res
            
            
            

  