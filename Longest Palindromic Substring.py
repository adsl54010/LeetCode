class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        anslen=1
        ans=s[0]
        for start in range (0,len(s)) :
            for end in range (len(s)-1,0,-1) :
                if end > start :
                    turnwork=0
                    if s[start] == s[end] :
                        turnwork=1
                        for shift in range (1,(int)((end-start+1)/2)) :
                            if s[start+shift] != s[end-shift] :
                                turnwork=0
                                break;
                    if turnwork == 1 :
                        if (end-start+1) > anslen :
                            ans=s[start:end+1]
                            anslen=len(ans)
                        break;
                else :
                    break
        return ans
