1. Thinking about the genPrimes generator from the last problem, which of the following can be done only by using a generator, instead of defining a function (that uses any type of construct we've learned about, except generators)?

Everything that can be done with generator can be done with a function

2. Every procedure that has a yield statement is a generator.

True

3. If a procedure has only one yield statement, but that statement will never be executed, then the procedure is not a generator.

False

4. Suppose we wanted to iterate over a million numbers using a 'for/in' loop. If we use the code for x in range(1000000), how many numbers do we need to store in memory at once?

1000000

5. If we were to use a generator to iterate over a million numbers, how many numbers do we need to store in memory at once?

2

# For the following tasks, would it be best to use a generator, a standard function, or either?

1. Finding the nth Fibonacci number

Standard function

2. Printing out an unbounded sequence of Fibonacci numbers

Generator

3. Printing out a bounded sequence of prime numbers, where the prime numbers are successively computed by division by smaller primes

Either a generator or standard function is fine

4. Printing out an unbounded sequence of prime numbers, where the prime numbers are successively computed by division by smaller primes

Generator

5. Finding the score of a word from the 6.00x Word Game of Pset 4

Standard function

6. Iterating over a sequence of numbers in a random order, where no number is repeated

Standard function