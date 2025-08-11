# Last updated: 8/11/2025, 11:12:32 AM
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def f(x):
            return "".join(sorted(str(x)))
        
        p = set()
        for i in range(32):
            num = pow(2,i)
            p.add(f(num))
        
        return f(n) in p