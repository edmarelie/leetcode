class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        stack = []

        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort(reverse=True)

        for pos, speed in pos_speed:
            time_taken = (target - pos) / speed
            stack.append(time_taken)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)