class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:

        #We calculate the time it takes for each car
        #We sort the positions and start at th end
        #Its specifically stated that a car will not take over, so if the time
        #is larger (takes longer to arrive) -- it is a new fleet
        time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
        res = cur = 0
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res