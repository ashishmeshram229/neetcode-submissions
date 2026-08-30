class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ""
        for i in strs :
            num = len(i)
            encoded_string+=str(num) + "#" + i
        return encoded_string



    def decode(self, s: str) -> List[str]:
        start = 0
        
        decoded_string = []
        while start < (len(s) ):
            curr = ""
            while s[start] != "#" :
                curr+=s[start]
                start+=1
            decoded_string.append(s[start+1 : start+int(curr)+1])
            start += int(curr)+1
        return decoded_string
            

                

            

