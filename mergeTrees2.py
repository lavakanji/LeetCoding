# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:22:29 2020

@author: kalan
"""

617. Merge Two Binary Trees

# =============================================================================
# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
# =============================================================================
1:58


Note: The merging process must start from the root nodes of both trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, tree1, tree2):
        if tree1 is None:
            return tree2
        if tree2 is None:
            return tree1 
        
        tree1.val += tree2.val
        tree1.left = self.mergeTrees(tree1.left, tree2.left)
        tree1.right = self.mergeTrees(tree1.right, tree2.right)
        
        return tree1
        
       
            
            
        


   
        
   
    
a=Solution()

a.mergeTrees(tree1,tree2)
