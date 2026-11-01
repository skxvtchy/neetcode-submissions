class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        res=0

        def isPrefixAndSuffix(x,y):
            diff = len(y)-len(x)
            
            if y[0:len(x)]==x and y[diff::]==x:

                return True

            return False
        
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                
               
                    res+=1

        return res