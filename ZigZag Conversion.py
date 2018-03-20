class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans=""
        if numRows > 2:
            for x in range (0,len(s),2*numRows-2) :
                ans+=s[x]
            for y in range (1,numRows) :
                for x in range (y,len(s),2*numRows-2) :
                    nextword=x+2*numRows-2-2*y
                    if (len(s) > nextword and nextword > x ):
                        ans+=s[x]
                        ans+=s[nextword]
                    else :
                        ans+=s[x]
        else :
            for y in range (0,numRows) :
                for x in range (y,len(s),numRows) :            
                    ans+=s[x]
        return ans    
