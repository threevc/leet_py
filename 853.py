# https://leetcode.com/problems/car-fleet/description/

# Beats has stopped
# Stack question, good intuition, stack the end time

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for x in range(len(speed)):
            pairs.append([position[x],speed[x]])
        
        pairs = sorted(pairs)[::-1]
        # for i, [p,s] in enumerate(pairs):
        for p,s in pairs:
            time = (target-p)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
