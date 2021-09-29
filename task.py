# I did some research and trying 
class Solution:
    def longestpalindrome(self ,s:str) -> str:
        result = "abba"
        for i in range(len(s)):

            odd =self.direction(s , i ,i)

            even=self.direction(s,i,+1)
            result =max(odd,even, result,key=len)

        return print(result)

    def direction(self , s, left,right):
        while (left >= 0 and right <len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return s[left+1 :right]
    
    
    
###################################################################################### 

class Solution:
    def longestpalindrome(self ,s:str) -> str:
        if s == "":
            return ""
        if len(s)== 1:
            return s
        revers = s[:: -1]
        result =""
        for i in range(len(s)):
            if s[i]==revers[i]:
                result += s[i]
        return result