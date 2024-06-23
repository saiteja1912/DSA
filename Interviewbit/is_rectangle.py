# A simple program to find if given 4 
# values can represent 4 sides of rectangle 
#m1
class Solution1:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        list=[A,B,C,D]
        list.sort()
        if(list[0]==list[1] and list[2]==list[3]):
            return 1
        return 0
#T:O(1), S:O(1)

#m2(efficient as it doesn't require additional space)
# Function to check if the given 
# integers value make a rectangle 
def isRectangle(a, b, c, d): 
    # Square is also a rectangle 
    if a == b == c == d: 
        return True
    elif a == b and c == d: 
        return True
    elif a == d and c == b: 
        return True
    elif a == c and d == b: 
        return True
    return False
class Solution2:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if(isRectangle(A,B,C,D)==True):
            return 1
        return 0
#T:O(1), S:O(1)

#m3
class Solution3:
    def solve(self, A, B, C, D):
        cnt = [0] * 4
        cnt[A] += 1
        cnt[B] += 1
        cnt[C] += 1
        cnt[D] += 1
        for i in range (4):
            if cnt[i] != 0 and cnt[i] != 2 and cnt[i] != 4:
                return 0
        return 1
    
s=Solution3()
print("It is a rectangle") if s.solve(1,1,2,1) else print("It is not a rectangle")