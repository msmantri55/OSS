# Radiation Exposure

"Radioactive decay" is the process by which an unstable atom loses energy and emits ionizing particles - what is commonly refered to as radiation. Exposure to radiation can be dangerous and is very important to measure to ensure that one is not exposed to too terribly much of it.

The radioactivity of a material decreases over time, as the material decays. A radioactive decay curve describes this decay. The x-axis measures time, and the y-axis measures the amount of activity produced by the radioactive sample. 'Activity' is defined as the rate at which the nuclei within the sample undergo transititions - put simply, this measures how much radiation is emitted at any one point in time. The measurement of activity is called the Becquerel (Bq). Here is a sample radioactive decay curve:

![Decay Curve](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/files_ps03_files_DecayCurve.png)

Now here's the problem we'd like to solve. Let's say Sarina has moved into a new apartment. Unbeknownst to her, there is a sample of Cobalt-60 inside one of the walls of the apartment. Initially that sample had 10 MBq of activity, but she moves in after the sample has been there for 5 years. She lives in the apartment for 6 years, then leaves. How much radiation was she exposed to?

We can actually figure this out using the radioactive decay curve from above. What we want to know is her total radiation exposure from year 5 to year 11.

![Start and stop time marked](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/files_ps03_files_DecayCurveMarked.png)

Total radiation exposure corresponds to the area between the two green lines at time = 5 and time = 11, and under the blue radioactive decay curve. This should make intuitive sense - if the x axis measures time, and the y axis measures activity, then the area under the curve measures (time * activity) = MBq*years, or, approximately the total number of MBq Sarina was exposed to in her time in the radioactive apartment (technically, this result is the combination of gamma rays and beta particles she was exposed to, but this gets a bit complicated, so we'll ignore it. Sorry, physicists!).

![Area we want to find](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/files_ps03_files_DecayCurveFill.png)

So far, so good. But, how do we calculate this? Unlike a simple shape - say a square, or a circle - we have no easy way to tell what the area under this curve is.

However, we have learned a technique that can help us here - *approximation*. Let's use an approximation algorithm to estimate the area under this curve! We'll do so by first splitting up the area into equally-sized rectangles (in this case, six of them, one rectangle per year):

![Approximating the area using rectangles](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/files_ps03_files_DecayCurveRectangles.png)

Once we've done that, we can figure out the area of each rectangle pretty easily. Recall that the area of a rectangle is found by multiplying the height of the rectangle by its width. The height of this rectangle:

![Area of one rectangle](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/files_ps03_files_Rectangle1.png)

is the value of the curve at 5.0. If the curve is described by a function, f, we can obtain the value of the curve by asking for f(5.0).

`f(5.0) = 5.181`

The width of the rectangle is 1.0. So the area of this single rectangle is `1.0*5.181 = 5.181`. To approximate how much radiation Sarina was exposed to, we next calculate the area of each successive rectangle and then sum up the areas of each rectangle to get the total. When we do this, we find that Sarina was exposed to nearly 23 MBq of radiation (technically, her apartment was bombarded by 23e6 \* 3.154e6 = 7.25e13 neutrons, for those interested...).

Whether or not this will kill Sarina depends exactly on the type of radiation she was exposed to (see [this link](http://web.mit.edu/newsoffice/2011/explained-radioactivity-0328.html) which discusses more about the ways of measuring radiation). Either way, she should probably ask her landlord for a substantial refund.

In this problem, you are asked to find the amount of radiation a person is exposed to during some period of time by completing the following function:

```
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
```

To complete this function you'll need to know what the value of the radioactive decay curve is at various points. There is a function `f` that will be defined for you that you can call from within your function that describes the radioactive decay curve for the problem. Do not define `f` in your code.

# Hangman

For this problem, you will implement a variation of the classic wordgame Hangman. For those of you who are unfamiliar with the rules, you may read all about it [here](http://en.wikipedia.org/wiki/Hangman%20%28game%29). In this problem, the second player will always be the computer, who will be picking a word at random.

In this problem, you will implement a **function**, called `hangman`, that will start up and carry out an interactive Hangman game between a player and the computer. Before we get to this function, we'll first implement a few helper functions to get you going.

For this problem, you will need the code files [`ps3_hangman.py`](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/ps3_hangman.py) and [`words.txt`](https://d37djvu3ytnwxt.cloudfront.net/asset-v1:MITx+6.00.1x_9+2T2016+type@asset+block/words.txt). Right-click on each and hit "Save Link As". Be sure to save them in same directory. Open and run the file `ps3_hangman.py` without making any modifications to it, in order to ensure that everything is set up correctly. By "open and run" we mean do the following:


* Go to Canopy. From the File menu, choose "Open".
* Find the file `ps3_hangman.py` and choose it.
* The template `ps3_hangman.py` file should now be open in Canopy. Click on it. From the Run menu, choose "Run File" (or simply hit Ctrl + R).

The code we have given you loads in a list of words from a file. If everything is working okay, after a small delay, you should see the following printed out:

```
Loading word list from file...
55909 words loaded.
```

If you see an `IOError` instead (e.g., "No such file or directory"), you should change the value of the `WORDLIST_FILENAME` constant (defined near the top of the file) to the **complete** pathname for the file `words.txt` (This will vary based on where you saved the file). Windows users, change the backslashes to forward slashes, like below.

For example, if you saved `ps3_hangman.py` and `words.txt` in the directory "C:/Users/Ana/" change the line: 

`WORDLIST_FILENAME` = "`words.txt`"  to something like

`WORDLIST_FILENAME` = "`C:/Users/Ana/words.txt`"

**This folder will vary depending on where you saved the files.**

The file `ps3_hangman.py` has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand how to use each helper function by reading the docstrings:

```
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
    .
    .
    .
# (end of helper code)
# -----------------------------------
```

You will want to do all of your coding for this problem within this file as well because you will be writing a program that depends on each function you write.

**Requirements**

Here are the requirements for your game:

1. The computer must select a word at random from the list of available words that was provided in `words.txt`. The functions for loading the word list and selecting a random word have already been provided for you in `ps3_hangman.py`.

The game must be interactive; the flow of the game should go as follows:

* At the start of the game, let the user know how many letters the computer's word contains.

* Ask the user to supply one guess (i.e. letter) per round.

* The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.

* After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
Some additional rules of the game:

* A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).

* A user loses a guess **only** when s/he guesses incorrectly.

* If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.

* The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.