"""Solution variants for Lesson 24: Scope
Correct answers for predictions:

1: 10
   → x is created inside example1 and returned. Simple.

2a: local
   → Inside example2, y = "local" creates a NEW local y.
2b: global
   → The global y was never changed! The function made its own y.

3: 42
   → Functions CAN read global variables. z exists outside, so it works.

4: Hello, World!
   → The parameter 'name' shadows the global 'name'.
     Inside the function, name is "World" (the argument), not "Charles".

5: NameError — 'secret' doesn't exist here!
   → 'secret' only exists inside example5. It's LOCAL.
     Once the function ends, it's gone.

6a: 3
   → .append() modifies the ORIGINAL list (mutation).
6b: ['apple', 'banana', 'cherry']
   → The list was changed! Lists are mutable, and the function
     received a reference to the SAME list.

7a: [10, 20, 30]
   → Inside the function, nums is reassigned to a NEW list.
7b: [1, 2, 3]
   → But the original 'numbers' is unchanged! Reassignment inside
     a function doesn't affect the outside variable.

KEY INSIGHT: Mutation (.append, .sort) changes the original.
             Reassignment (=) creates a new local variable.
"""
