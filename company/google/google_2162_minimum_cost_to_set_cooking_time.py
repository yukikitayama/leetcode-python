class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        def compute_cost(min, sec):

            # Make microwave display time
            s = str(min * 100 + sec)

            curr = str(startAt)
            cost = 0

            for c in s:

                # If current digit is equal to the digit we want, push
                if c == curr:
                    cost += pushCost
                # Move finger and push the new digit if the current digit is not what we want
                else:
                    cost += (moveCost + pushCost)
                    # We moved our finger to the new digit, so update current digit
                    curr = c

            return cost

        # Get minutes part from total seconds
        max_min = targetSeconds // 60
        ans = float('inf')

        for min_ in range(max_min + 1):
            # Get seconds part from the total seconds minus minutes
            sec = targetSeconds - min_ * 60

            # print(f'min_: {min_}, sec: {sec}')

            # Microwave display has constraints that minutes and seconds can display unto 99
            # In that case, skip
            if sec > 99 or min_ > 99:
                continue

            ans = min(ans, compute_cost(min_, sec))

        return ans


if __name__ == '__main__':
    startAt = 1
    moveCost = 2
    pushCost = 1
    targetSeconds = 600
    startAt = 0
    moveCost = 100000
    pushCost = 100000
    targetSeconds = 5678
    # 800000
    print(Solution().minCostSetTime(startAt, moveCost, pushCost, targetSeconds))
