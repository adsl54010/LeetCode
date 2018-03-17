class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1len=len(nums1)
        nums2len=len(nums2)
        smallnum,medinum=divmod(nums1len+nums2len,2)
        crusmall=1
        crunums1=0
        crunums2=0
        smallnum+=medinum
        while crusmall < smallnum :
            if crunums1 < nums1len:
                print(crunums1)
                if crunums2 < nums2len:
                    if (nums1[crunums1] < nums2[crunums2]) :
                        crunums1+=1
                    else :
                        crunums2+=1
                else :
                    crunums1+=1                        
            else :
                    crunums2+=1                    
            crusmall+=1
        if medinum == 1:
            if crunums1 < nums1len:
                if crunums2 < nums2len:            
                    if (nums1[crunums1] < nums2[crunums2]):
                        return float(nums1[crunums1])
                    else :
                        return float(nums2[crunums2])
                else :
                    return float(nums1[crunums1])
            else :
                return float(nums2[crunums2])
        else :
            if crunums1 < nums1len:
                if crunums2 < nums2len:        
                    if (nums1[crunums1] < nums2[crunums2]):
                        ans1=nums1[crunums1]
                        crunums1+=1
                    else :
                        ans1=nums2[crunums2]
                        crunums2+=1
                else :
                    ans1=nums1[crunums1]
                    crunums1+=1
            else :
                ans1=nums2[crunums2]
                crunums2+=1
            if crunums1 < nums1len:
                if crunums2 < nums2len:
                    if (nums1[crunums1] < nums2[crunums2]):
                        return (nums1[crunums1]+ans1)/2
                    else :
                        return (nums2[crunums2]+ans1)/2
                else :
                    return (nums1[crunums1]+ans1)/2                    
            else :
                return (nums2[crunums2]+ans1)/2
