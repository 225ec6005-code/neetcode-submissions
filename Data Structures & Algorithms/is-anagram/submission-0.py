
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable_1={}
        hashtable_2={}
        for ch in s:
            if ch in hashtable_1:
                hashtable_1[ch]+=1
            else:
                hashtable_1[ch]=1    
        for ch in t:
            if ch in hashtable_2:
                hashtable_2[ch]+=1
            else:
                hashtable_2[ch]=1 
        
        if hashtable_1 == hashtable_2:
            return True
        else:
            return False    
