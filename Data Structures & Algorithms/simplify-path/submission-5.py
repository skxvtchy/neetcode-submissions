class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack=[]
        res =""
        for i in path.split("/"):
            if i == "" or i== '.':
                continue
            if i=="..":
                if stack:
                    stack.pop()
                continue
            stack.append(i)


        for i in stack:
            res+="/"
            res+=i
        
        if res:
            return res
        return "/"