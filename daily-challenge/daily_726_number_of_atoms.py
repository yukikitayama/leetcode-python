import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [collections.defaultdict(int)]

        i = 0

        while i < len(formula):

            if formula[i] == "(":
                stack.append(collections.defaultdict(int))
                i += 1

            elif formula[i] == ")":
                curr_map = stack.pop()
                i += 1

                # Extract digit
                multiplier = ""
                while i < len(formula) and formula[i].isdigit():
                    multiplier += formula[i]
                    i += 1

                # Increment atom count if we have digit
                if multiplier:
                    multiplier = int(multiplier)
                    # Increment all the atom counts
                    for atom in curr_map:
                        curr_map[atom] *= multiplier

                # Add current map to the previous map
                for atom, count in curr_map.items():
                    stack[-1][atom] += count

            # Always start with uppercase
            else:
                # This is uppercase
                curr_atom = formula[i]
                i += 1

                # Extract lowercase
                while i < len(formula) and formula[i].islower():
                    curr_atom += formula[i]
                    i += 1

                # Extract digit
                curr_count = ""
                while i < len(formula) and formula[i].isdigit():
                    curr_count += formula[i]
                    i += 1

                # Update atom count
                if curr_count == "":
                    stack[-1][curr_atom] += 1
                else:
                    stack[-1][curr_atom] += int(curr_count)

        atom_to_count = stack[0]
        sorted_atoms = sorted(atom_to_count.keys())
        ans = []

        for atom in sorted_atoms:
            ans.append(atom)
            if atom_to_count[atom] > 1:
                ans.append(str(atom_to_count[atom]))

        return "".join(ans)