from typing import List
import collections
import heapq


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_to_max_heap = collections.defaultdict(list)
        self.food_to_rating = collections.defaultdict(int)
        self.food_to_cuisine = collections.defaultdict(str)
        for i in range(len(foods)):
            self.food_to_rating[foods[i]] = ratings[i]
            self.food_to_cuisine[foods[i]] = cuisines[i]
            # Heapify
            heapq.heappush(self.cuisine_to_max_heap[cuisines[i]], (-1 * ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        max_heap = self.cuisine_to_max_heap[cuisine]
        heapq.heappush(max_heap, (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        max_heap = self.cuisine_to_max_heap[cuisine]
        top_rate, top_food = max_heap[0]
        top_rate *= -1

        while top_rate != self.food_to_rating[top_food]:
            heapq.heappop(max_heap)
            top_rate, top_food = max_heap[0]
            top_rate *= -1

        return top_food


if __name__ == "__main__":
    foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
    cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
    ratings = [9, 12, 8, 15, 14, 7]
    foodRatings = FoodRatings(foods, cuisines, ratings)

    print(foodRatings.food_to_rating)
    print(foodRatings.food_to_cuisine)
    print(foodRatings.cuisine_to_max_heap)

    print(foodRatings.highestRated("korean"))
    print(foodRatings.highestRated("japanese"))
    foodRatings.changeRating("sushi", 16)
    print(foodRatings.highestRated("japanese"))
    foodRatings.changeRating("ramen", 16)
    print(foodRatings.highestRated("japanese"))
