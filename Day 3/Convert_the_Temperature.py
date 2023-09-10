class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        tempk = celsius + 273.15
        tempf = celsius * 1.80 + 32.00
        ans = [tempk,tempf]
        return ans
