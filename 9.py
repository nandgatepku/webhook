class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        p=str(x)
        po=p[::-1]
        m=int(po)
        if m==x:
            return True
        else:
            return False