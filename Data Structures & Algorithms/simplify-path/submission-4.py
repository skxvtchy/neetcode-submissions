class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = ""
        path+="/"

        res =""
        l=0

        for i in range(1,len(path)):
            if path[i]=="/":
                # print(path[i])
                if word:
                    print(word)
                    if word[0]==".":
                        if len(word)==2 and stack:
                            stack.pop()
                        elif len(word)>2:
                            stack.append(word)
                    elif word[0]!=".":
                        stack.append(word)
                    word=""
            else:
                # print(path[i])

                word += path[i]

        
        for i in stack:
            res+="/"
            res+=i
        
        if res:
            return res
        else:
            return "/"