# State Machine

## Deterministic Finite Automation (DFA)

- `State machine` reads some input and changes the states based on those inputs.
- `Transition` is the change in a state.
- `Finite state machine` is the state machine with a finite number of states.
- `Deterministic finite automation (DFA)` is the finite state machine that either `accept` or `reject` a sequence of
   states.
  - e.g. Traffic light. "Green -> Yellow -> Red -> Green" are accepted each time in the sequence. But "Green -> Yellow
    -> Red -> Yellow" is rejected when Red changes into Yellow.
- There is only one path for the specific input from the current state to the next state.

#### Problem

- [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
- [65. Valid Number](https://leetcode.com/problems/valid-number/)
- [520. Detect Capital](https://leetcode.com/problems/detect-capital/)
- [890. Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)
- [1018. Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)
