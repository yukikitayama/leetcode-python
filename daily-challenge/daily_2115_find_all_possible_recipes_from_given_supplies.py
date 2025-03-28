from typing import List
import collections


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies)
        adj = collections.defaultdict(list)
        indegree = [0] * len(recipes)
        for i, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in supplies_set:
                    # bread -> sandwitch
                    adj[ingredient].append(recipes[i])
                    indegree[i] += 1

        queue = collections.deque(i for i, c in enumerate(indegree) if c == 0)
        recipe_to_idx = {recipe: i for i, recipe in enumerate(recipes)}
        ans = []
        while queue:
            i = queue.popleft()
            recipe = recipes[i]
            ans.append(recipe)

            for next_recipe in adj[recipe]:
                indegree[recipe_to_idx[next_recipe]] -= 1
                if indegree[recipe_to_idx[next_recipe]] == 0:
                    queue.append(recipe_to_idx[next_recipe])

        return ans