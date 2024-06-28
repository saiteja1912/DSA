class Solution:
    def reverseBits(self, n: int) -> int:
        rev=0
        for i in range(32):
            #get unit place of n
            bit=n&1
            #accomodate space for this bit in rev
            rev=rev<<1
            #include bit in rev
            rev=rev|bit
            #get the ten's place of n to units place
            n=n>>1
        return rev
    
s=Solution()
print(s.reverseBits(4))
