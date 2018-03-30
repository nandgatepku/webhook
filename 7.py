class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<-2**31:
            return 0
        if x>2**31-1:
            return 0
        if x<0:
            x=abs(x)
            p=str(x)
            po=p[::-1]
            pi=int(po)
            y=-pi
            if y<-2**31:
                return 0
            if y>2**31-1:
                return 0
            return y
        else:
            p=str(x)
            po=p[::-1]
            pi=int(po)
            if pi<-2**31:
                return 0
            if pi>2**31-1:
                return 0
            return pi
        