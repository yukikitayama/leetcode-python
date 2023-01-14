from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:

        max_damage = max(damage)
        sum_damage = sum(damage)

        if armor > max_damage:
            sum_damage -= max_damage
        else:
            sum_damage -= armor

        return sum_damage + 1


if __name__ == '__main__':
    damage = [2,7,4,3]
    armor = 4
    damage = [2, 5, 3, 4]
    armor = 7
    print(Solution().minimumHealth(damage, armor))

