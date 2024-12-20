The repository contains different functions which implements recursive generating in different ways.

recursive_generator.py:
  - genTuple(k, n) : generates all possible tuples of length k on range from 0 to n including. In the tuple the values can repeat.
  - genTupleNoRep(k, n) : generates all possible tuples of length k on range from 0 to n including. In the tuple the values cannot repeat.
  - genGrowingSequence(k, n) : generates all possible growing sequences of length k on range from 0 to n including.
  - genNonDecreasingSequence(k, n) : generates all possible non decreasing sequences of length k on range from 0 to n including.
  - genSequenceFromSet(k, items) : generates all possible sequences of length k from list of items
  - genSequenceFromSetLimitedRep(k, dic) : generates all possible sequences of length k from dictionary, where key is the element of output sequence and value is the
    number of repetitions of this element in the output sequence.

 decompose_the_number.py:
  - decomposeTheNumber(n) : generates all posible decompositions of the number n as a sum of output sequence. Different order of additions means that decompositions are different.
  - decomposeTheNumber2(n) : generates all posible decompositions of the number n as a sum of output sequence. Different order of additions means that decompositions are different.
    The difference between this and previous one, that this function is more effective, as it calls recursion only on fraction
  - decomposeTheNumberByK(n, k) : generates all posible decompositions of the number n as a sum of output sequence, k is the number of additions which we can use. Different order
    of additions means that decompositions are different.
  - decomposeTheNumberNonDecreasing(n) : generates all posible decompositions of the number n as a sum of output sequence. Output list is non-decreasing.
