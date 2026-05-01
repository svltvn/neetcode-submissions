class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures), 1):
                if temperatures[j] > temperatures[i]:
                    days[i]=j-i
                    break
                elif j == len(temperatures)-1:
                    days[i]=0
        return days
        