class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        def nextDay(days):
            newDays = [0] * len(cells) 
            for i in range(1, len(days) - 1):
                if (days[i - 1] == 1 and days[i + 1] == 1 or 
                    days[i - 1] == 0 and days[i + 1] == 0):
                    newDays[i] = 1
            return newDays
        seen = {}
        days = 0
        while days < n:
            state = tuple(cells)
            if state in seen:
                cycle_start = seen[state]
                cycle = days - seen[state]
                remainer = cycle_start + (n - cycle_start) % cycle    
                for c, d in seen.items():
                    if d == remainer:
                        return c
            seen[state] = days
            cells = nextDay(cells)
            days += 1
        return cells
    
    
            
        
