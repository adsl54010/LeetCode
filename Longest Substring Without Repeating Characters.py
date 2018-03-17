class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max=0
        havestring=""
        for i in range (0,len(s)):
            if havestring.find(s[i]) != -1:
                if len (havestring)>max:
                    max=len(havestring)
                havestring=havestring[havestring.find(s[i])+1:]
            havestring+=(s[i])
        if len (havestring)>max:
            max=len(havestring)
        return max
