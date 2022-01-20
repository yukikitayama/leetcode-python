# Programming

## Functional Programming

- Use recursion instead of loops
- Like to use array
- Use `pure function`.
  - `Pure function` is a function that does not modify global variables or objects.
  - It produces an output only depending on the input.
  - People also describes it as it has no `side effect`

## Short-Circuit Evaluation

- The function returns as soon as it finds a false value without processing the rest of the items in iterable.
- e.g. Python built-in function `all()` is implemented using `short-circuit evaluation`. `all([1, 1, 0, 1, 1])` returns
  false as soon as it finds 0 in the iterable, so the rest of the 1s are ignored.