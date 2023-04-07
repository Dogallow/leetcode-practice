def climbStairs(self, n: int) -> int:
    memo = {}


    def countSteps(count):
        if count in memo: return memo[count]
        if count == n: 
            return 1
        if count > n: return 0

        total1 = countSteps(count + 1) 
        total2 = countSteps(count + 2)

        memo[count] = total1 + total2
        
        return memo[count]
    
    return countSteps(0)

