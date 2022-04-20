import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        counter = collections.Counter(s)

        # -v to make max heap
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)

        prev_freq = 0
        prev_char = ''
        while heap:

            curr_freq, curr_char = heapq.heappop(heap)

            # Add current character to answer
            ans.append(curr_char)
            # Increment because freq is negative for max heap
            # we just use current character, so we need to update frequency
            curr_freq += 1

            # This previously postpone character and its freq go to heap
            # frequency is negative value because of max heap
            # So if it's negative, we still need to add this character to answer
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            # Postpone current character use, because we cannot place them side by side
            prev_freq = curr_freq
            prev_char = curr_char

        ans = ''.join(ans)
        if len(ans) == len(s):
            return ans
        else:
            return ''


if __name__ == '__main__':
    s = 'aab'
    s = 'aaab'
    print(Solution().reorganizeString(s))
