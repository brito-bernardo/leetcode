class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> str:
        sorted_data = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
    

        sorted_names = [name for name, _ in sorted_data]

        return sorted_names
