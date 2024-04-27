class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        best_steps = {}

        def count_steps(curr, next_):
            steps_between = abs(curr - next_)
            # [0, 1, 2, 3, 4], curr: 1, next_: 4,
            # steps_between: 3, steps_around: 5 - 3 = 2
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        def try_lock(ring_index, key_index):

            # Memoization
            if (ring_index, key_index) in best_steps:
                return best_steps[(ring_index, key_index)]

            # Base
            if key_index == key_len:
                best_steps[(ring_index, key_index)] = 0
                return best_steps[(ring_index, key_index)]

            # State transition
            min_steps = float("inf")
            for char_index in range(ring_len):

                if ring[char_index] == key[key_index]:
                    min_steps = min(
                        min_steps,
                        # +1 for pressing a button
                        count_steps(ring_index, char_index) + 1 + try_lock(char_index, key_index + 1)
                    )

            best_steps[(ring_index, key_index)] = min_steps

            return best_steps[(ring_index, key_index)]

        return try_lock(0, 0)
