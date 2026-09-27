class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def find_char_count(a):
            dictionary={}
            box=list(a)
            for char in box:
                if char in dictionary:
                    dictionary[char] +=1
                else:
                    dictionary[char]=1
            return dictionary
            
        count_s=find_char_count(s)
        count_t=find_char_count(t)
        keys_list=list(count_s.keys())
        x=len(count_s)
        if len(count_s)!=len(count_t):
            return False
        else:
            y=0
            while y!=x:
                current_key=keys_list[y]
                if current_key in count_t and count_s[current_key]==count_t[current_key]:
                    y +=1
                else:
                    return False
        return True
                