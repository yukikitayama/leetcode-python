from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0

        for num in data:

            # bin_rep = bin(num)[-8:]
            bin_rep = format(num, '#010b')[-8:]

            if n_bytes == 0:

                for bit in bin_rep:

                    if bit == '0':
                        break
                    n_bytes += 1

                # If 1 byte characters
                if n_bytes == 0:
                    continue

                if n_bytes == 1 or n_bytes > 4:
                    return False

            else:
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            n_bytes -= 1

        return n_bytes == 0


if __name__ == '__main__':
    print(bin(197), bin(130), bin(1))
    print(format(197, '#010b'))
    print(format(197, 'b'))
    print(format(1, '#010b'))
    print(bin(197)[-8:])
    data = [197, 130, 1]
    # data = [235, 140, 4]
    print(Solution().validUtf8(data))
