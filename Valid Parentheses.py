class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        temp=[]
        for x in s :
            if x== "(" or x== "[" or x=="{" :
                temp.append(x)
                continue
            elif x== ")" or x== "]" or x=="}" :
                if len(temp)==0:
                    return False
                else :
                    temppop=temp.pop()
                    if x== ")" and temppop=="("  or (x=="]" and temppop=="[") or (x=="}" and temppop=="{") :
                        continue
                    else :
                        return False
        if len(temp)==0:
            return True 
        else :
            return False
