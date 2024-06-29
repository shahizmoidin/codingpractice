class Solution(object):
    def lengthOfLastWord(self, s):
       sb=s.strip().split(" ")
       k=len(sb)
       h=sb[k-1]
       return len(h)
       