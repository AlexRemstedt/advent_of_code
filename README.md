# Personal Project: Advent_of_Code
Advent of code challenge for self practice


## Introduction
I have taken the challenge upon myself to finish the [**Advent of Code 2020**](https://adventofcode.com/2020) coding
challenge (late however). This is because I want to maintain my Python programming skills.
For each objective I will write a short summary of how I tackled the problem and what I encountered as being difficult.
It is my objective to make my code as efficient and effective as possible.


### Day 1
Day 1 asks you to find either two or three digits that sum up to 2020.
I had problems with finding a way to read a large file as I did not want to manually insert every entry given.
Quickly I had found the `open()`, `readlines()` and `close()`, which solved that problem.
The actual code was not hard to construct, I do however think there must be a more elegant way to cycle through a loop
with double occurunces.

### Day 2
Day 2 asks you to find the correct password. The challenge here is you get a list of strings which contain numbers and
string pieces. You need to find a way to select certain parts within the string for this to actually work.
I managed to do this by using `find()`, and using the index to store each important part of the string in its
own variable. Part 1 and 2 are very similar, the only difference is the if-case.
