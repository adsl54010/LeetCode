class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        DP=[ [False] * (len(p) + 1) for x in range (len(s) + 1) ]
        DP[0][0]=True
        
        for pindex in range (2,(len(p) + 1) ) :
            if p[pindex-1] == "*" :
                DP[0][pindex] = DP[0][pindex-2]
        
        for pindex in range (1,(len(p) + 1) ) :
            for sindex in range (1, (len(s) + 1) ) :
                if p[pindex - 1] == "." :
                    DP[sindex][pindex] = DP[sindex -1][pindex -1]  
                elif p[pindex - 1] == "*" :
                    DP[sindex][pindex ] =  DP[sindex][pindex -2] or DP[sindex][pindex - 1] 
                    if p[pindex - 2] == s[sindex-1] or p[pindex-2] == "." :
                        DP[sindex][pindex ] = DP[sindex][pindex ] or DP[sindex -1][pindex ]
                else :
                    if s[sindex -1] == p[pindex -1] and DP[sindex-1][pindex-1] :
                        print(s[sindex -1]," ",p[pindex -1]," ",DP[sindex-1][pindex-1] )
                        DP[sindex][pindex] = True
        return DP[len(s)][len(p)]
                
