def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        currentCost = 0
        def countCost(index):
            nonlocal currentCost
            value = 0
            if index >= len(cost):
                return 0
            lowest = min(countCost(index + 1), countCost(index + 2))
            print(f"Lowest: {lowest}")
            
            if index < 0:
                if index == -1:
                    return lowest
                lowest_2 = lowest + cost[index] 
                print(f"Lowest_2 : {lowest_2} \n Lowest : {lowest} \n Index : {index}")
                if lowest_2 < lowest and lowest_2 <= lowest + cost[index]:
                    return lowest_2
            else:
                lowest += cost[index]
            print(f"Lowest Plus the cost of the current step: {lowest}")
            # one_step = countCost(index + 1)
            # print(f"One Step: {one_step}")
            # two_step = countCost(index + 2)
            # print(f"Two Step: {two_step}")
            # one_step += cost[index]
            # two_step += cost[index]
            
            
            return lowest

        
        return countCost(-1)
