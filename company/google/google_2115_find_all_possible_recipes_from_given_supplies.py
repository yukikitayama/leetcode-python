"""
- Directional graph
"""


from typing import List
import collections


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)

        ans = []

        ingredient_to_recipe = collections.defaultdict(set)
        in_degree = collections.Counter()

        for recipe, ingredient in zip(recipes, ingredients):
            non_available = 0

            for ing in ingredient:
                if ing not in available:
                    non_available += 1
                    ingredient_to_recipe[ing].add(recipe)

            if non_available == 0:
                ans.append(recipe)
            else:
                in_degree[recipe] = non_available

        # print(f'ans: {ans}')
        # print(f'Before: {in_degree}')
        # print(f'Before: {ingredient_to_recipe}')

        # recipe in ans are the recipe with indegree 0
        for rcp in ans:

            # print(f'  rcp: {rcp}')

            # Remove rcp from the dictionary if found
            # If not found, use empty set
            for recipe in ingredient_to_recipe.pop(rcp, set()):
                # If the rcp doesn't exist, it doesn't affect the existing dictionary
                in_degree[recipe] -= 1

                if in_degree[recipe] == 0:
                    ans.append(recipe)

        # print(f'After: {in_degree}')
        # print(f'After: {ingredient_to_recipe}')

        return ans


class Solution1:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []

        seen = set(supplies)

        queue = collections.deque([(recipe, ingredient) for recipe, ingredient in zip(recipes, ingredients)])

        prev_size = len(seen) - 1

        # Every time we create a new recipe, we have more items in seen than previous seen
        # But when we cannot create any more new recipe, seen does not grow,
        # so terminate while loop when len(seen): current items size == previous item size
        while len(seen) > prev_size:

            prev_size = len(seen)

            for _ in range(len(queue)):

                recipe, ingredient = queue.popleft()

                # If we have all the ingredients in seen to make current recipe
                if all(i in seen for i in ingredient):
                    # We can create current recipe
                    ans.append(recipe)
                    # Add the current recipe to seen as ingredient for other recipe
                    seen.add(recipe)

                # If we currently cannot create the current recipe
                # we still put it into queue, because in the next iteration
                # we could have enough ingredients by the above if statement
                # so give the next chance
                else:
                    queue.append((recipe, ingredient))

            # print(f'prev_size: {prev_size}, len(seen): {len(seen)}, seen: {seen}')

        return ans


if __name__ == '__main__':
    recipes = ["bread"]
    ingredients = [["yeast", "flour"]]
    supplies = ["yeast", "flour", "corn"]
    # ["bread"]
    recipes = ["bread", "sandwich"]
    ingredients = [["yeast", "flour"], ["bread", "meat"]]
    supplies = ["yeast", "flour", "meat"]
    # ["bread", "sandwich"]
    recipes = ["bread", "sandwich", "burger"]
    ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
    supplies = ["yeast", "flour", "meat"]
    # ["bread", "sandwich", "burger"]
    print(Solution().findAllRecipes(recipes, ingredients, supplies))
