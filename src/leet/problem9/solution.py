class Solution(object):
    def __init__(self, id, name, difficulty):
        self.id = id
        self.name = name
        self.difficulty = difficulty  
    
    def isPalindrome(self, x: int) -> bool:
        is_palindrome = False
        
        if x == 0:
            is_palindrome = True
        elif x > 0:
            int_str = str(x)
            print('int_str: ', int_str)

            int_str2 = "".join(reversed(int_str)) 
            print ('int_str2: ', int_str2)

            palindrome = int(int_str2)
            print('palindrome: ', palindrome)
            
            if x == palindrome:
                is_palindrome = True
        elif x < 0:
            is_palindrome = False
        
        return is_palindrome
