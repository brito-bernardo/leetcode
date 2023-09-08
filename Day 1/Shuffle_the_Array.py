class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array_final = []
        j = 0
        #divide
        array1 = nums[0 : n]
        array2 = nums[n:]
        while j < n:
            array_final.append(array1[j])
            array_final.append(array2[j])
            j += 1
        return array_final


        
        