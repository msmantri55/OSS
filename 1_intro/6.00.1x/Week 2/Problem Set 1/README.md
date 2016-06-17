#Counting Vowels

Assume `s` is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: '`a`', '`e`', '`i`', '`o`', and '`u`'. For example, if `s = 'azcbobobegghakl'`, your program should print:

    Number of vowels: 5

For problems such as these, do not include `raw_input` statements or define the variable `s` in any way. Our automated testing will provide a value of `s` for you - so the code you submit in the following box should assume `s` is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

#Counting Bobs

Assume `s` is a string of lower case characters.

Write a program that prints the number of times the string '`bob`' occurs in s. For example, if `s` = '`azcbobobegghakl`', then your program should print

    Number of times bob occurs is: 2

For problems such as these, do not include `raw_input` statements or define the variable `s` in any way. Our automated testing will provide a value of `s` for you - so the code you submit in the following box should assume `s` is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

#Counting and Grouping

A catering company has hired you to help with organizing and preparing customer's orders. You are given a list of each customer's desired items, and must write a program that will count the number of each items needed for the chefs to prepare. The items that a customer can order are: salad, hamburger, and water.

Write a function called `item_order` that takes as input a string named `order`. The string contains only words for the items the customer can order separated by one space. The function returns a string that counts the number of each item and consolidates them in the following order: `salad:[# salad] hamburger:[# hambruger] water:[# water]`

If an order does not contain an item, then the count for that item is 0. Notice that each item is formatted as `[name of the item][a colon symbol][count of the item]` and all item groups are separated by a space.

For example:

  If `order = "salad water hamburger salad hamburger"` then the function returns `"salad:2 hamburger:2 water:1"`
  If `order = "hamburger water hamburger"` then the function returns `"salad:0 hamburger:2 water:1"`