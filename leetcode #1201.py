import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        small = min(a,b,c)
        left,right=small,small*n
        ab,ac,bc=(a*b)//math.gcd(a,b),(a*c)//math.gcd(a,c),(c*b)//math.gcd(c,b)
        abc=(c*ab)//math.gcd(ab,c)
        while(left<right):
            mid=left+(right-left)//2
            pos=mid//a+mid//b+mid//c-mid//ab-mid//ac-mid//bc+mid//abc
            if pos>=n:
                right=mid
            else:
                left=mid+1
        return left