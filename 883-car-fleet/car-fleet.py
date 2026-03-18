class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [] # stack to store all possible fleets
        posSpeed = [(position[i], speed[i]) for i in range(len(position))]
        posSpeed.sort(key=lambda x: x[0], reverse=True)
        # print(posSpeed)
        for p, s in posSpeed:
            # print(fleet)
            time = (target - p)/s
            while fleet and fleet[-1] >= time:
                time = max(fleet.pop(), time)
            fleet.append(time)
        return len(fleet)