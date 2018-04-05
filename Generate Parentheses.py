class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def choseparentheses(ln,rn):
            ans=[]
            if ln>0:
                ans1=choseparentheses(ln-1,rn)
                for i in range (0,len(ans1)):
                    ans.append('('+ans1[i])
            if rn>ln:
                ans2=choseparentheses(ln,rn-1)
                for i in range (0,len(ans2)):
                    ans.append(')'+ans2[i])
            if rn==0 :
                ans.append('')
            return ans
        return choseparentheses(n,n)
