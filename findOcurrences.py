# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:53:25 2020

@author: kalan
"""

#1078. Occurrences After Bigram
#Easy

# =============================================================================
# Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.
# 
# For each such occurrence, add "third" to the answer, and return the answer.
# 
#  
# 
# Example 1:
# 
# Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
# Output: ["girl","student"]
# Example 2:
# 
# Input: text = "we will we will rock you", first = "we", second = "will"
#Output: ["we","rock"]
# =============================================================================


#7-01
#end - 7:09 --accepted/submission runtime error -7:13..second submission;7:16 submissoin accepted



class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text_l = text.split()
        out=[]
        for i in range(0,len(text_l)):
            if i+2 < len(text_l):
                if text_l[i] == first and text_l[i+1] == second:
                    #print(text_l[i+2])
                    out.append(text_l[i+2])
        return out

a=Solution()

# =============================================================================
# text = "alice is a good girl she is a good student"
# first = "a"
# second = "good"
# 
# text = "we will we will rock you"
# first = "we" 
# second = "will"
# =============================================================================

text = "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"

first="kcyxdfnoa"
second = "jkypmsxd"

a.findOcurrences(text, first, second)
        
       