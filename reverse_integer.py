class Solution:
    def reverse(self, x):
        
        if x < 0:
            reversed_int = str(x)[0]+str(x)[:0:-1]
            back_to_it = int(reversed_int)
            if back_to_it <= -2**31:
                return 0
            return back_to_it
        else:
            reversed_int = str(x)[::-1]
            back_to_it = int(reversed_int)
            if back_to_it >= 2**31 - 1:
                return 0
            return back_to_it