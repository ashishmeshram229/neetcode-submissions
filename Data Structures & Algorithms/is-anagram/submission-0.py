class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs= {}
        if len(s) != len(t):
            return False

        for i in s :
            if i in hashs :
                hashs[i]+=1
            else :
                hashs[i] = 1
        for j in t :
            if j in hashs :
                hashs[j]-=1
            
        for key, values in hashs.items() :
            if values !=0 :
                return False
        return True
        