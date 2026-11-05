class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # we need one loop going over the nums array => [ 1,2,3,3]
        # then we need another loop comparing the values
        len(nums)
        numsSet = set()
      
        for num in nums:
            numsSet.add(num)
        
        return len(numsSet) < len(nums)
       
        #return len(set(nums)) < len(nums)

