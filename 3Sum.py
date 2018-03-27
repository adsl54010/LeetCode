class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rtype = []
        temp=[None] * 3
        nums.sort()
        numslen=len(nums)
        for x in range (0,numslen-2) :
            if nums[x] >0 :
                break
            if x>0 and nums[x]==nums[x-1] :
                continue
            y,z=x+1,numslen-1
            while y<z :
                total=nums[x]+nums[y]+nums[z]
                if total <0 :
                    y+=1
                    continue
                elif total>0 :
                    z-=1
                else:
                    rtype.append([nums[x],nums[y],nums[z]])
                    while y<z and nums[y+1]==nums[y]:
                        y+=1
                    while z>y and nums[z-1]==nums[z]:
                        z-=1  
                    y+=1
                    z-=1
        return rtype
