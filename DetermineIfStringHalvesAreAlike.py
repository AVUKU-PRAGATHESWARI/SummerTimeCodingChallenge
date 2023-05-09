class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v=['a','e','i','o','u','A','E','I','O','U']
        first=s[:len(s)//2]
        second=s[len(s)//2:]
        count1=0
        count2=0
        for i in first:
            if i in v:
                count1+=1
        for j in second:
            if j in v:
                count2+=1
        if count1==count2:
            return 1
        else:
            return 0