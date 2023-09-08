class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        array_pos = []
        array_neg =[]
        array_final = []

        for i in nums:
            if i > 0:
                array_pos.append(i)
            else:
                array_neg.append(i)

        for i in range (len(array_pos)):
            array_final.append(array_pos[i])
            array_final.append(array_neg[i])
        return array_final

