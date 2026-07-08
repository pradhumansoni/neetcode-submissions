class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' NOTE -> This is a 1-Indexed Array index starts from 1
            Using 2 Pointers Pattern To solve it.     
        '''
        i = 0
        j = len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1] 
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1