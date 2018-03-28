class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def numtoword(numb,words) :        
            newwords=[]

            if numb=="2":
                word=["a","b","c"]
            elif numb=="3" :
                word=["d","e","f"]
            elif numb=="4" :
                word=["g","h","i"]
            elif numb=="5" :
                word=["j","k","l"]
            elif numb=="6" :
                word=["m","n","o"]
            elif numb=="7" :
                word=["p","q","r","s"]
            elif numb=="8" :
                word=["t","u","v"]
            elif numb=="9" :
                word=["w","x","y","z"]
            for x in words:
                for y in word:
                    addword=x+y
                    newwords.append(addword)
            return newwords
        
        if len(digits)>0:
            words=[""]
        else :
            words=[]
        for x in digits :
            words=numtoword(x,words)
        return words
            
        
            
