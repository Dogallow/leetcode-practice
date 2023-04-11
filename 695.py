def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # I want to implement a set. This could help with keeping track of the coordinates, and help handle duplicates.
    # I believe we need to iterate through the entire grid.
        # When we iterate through the grid. We want to see if the value of the coordinate is 1. We want to enter our helper function.
    # Need to think about edge cases. Possibly there are no islands, there is no grid to begin with. Possibly the whole grid is a island.
    if len(grid) == 0: return 0
    
    island_set = set()
    max_island = 0

    
    def mapOutIsland(row, col):
        nonlocal max_island
        # We have to have a way to track the amount of land we visit in one recursion.
        total = 0
        if grid[row][col] == 0:
            return 0
        
        # Handle case where you revisit an island coordinate
        if tuple([row, col]) in island_set:
            return 0;
        
        # If the current coord is a value of one and has passed our checks up above(the value is not 0, already visited the coord)
        if grid[row][col] == 1:
            island_set.add((row, col))
            total += 1
        
        # Look Up
        # Handle case if the row is the first row. Then You can't look up.
        if row != 0:
            total += mapOutIsland(row - 1, col)
        

        # Look Down
        # Handle case if the row is the last row. Then you can't look down.
        if row != len(grid) - 1:
            total += mapOutIsland(row + 1, col)
        
        # Look Left
        # Handle case if the column is the first column. Then you can't look left.
        if col != 0:
            total += mapOutIsland(row, col - 1)

        # Look right
        # Handle case if the column is the last column. Then you can't look right.
        if col != len(grid[row]) - 1:
            total += mapOutIsland(row, col + 1)

        if total > max_island:
            max_island = total
        return total

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if tuple([i, j]) not in island_set:
                    mapOutIsland(i, j)
        
    return max_island
