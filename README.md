# Oh Hell! Scoring

Python scoring script for Oh Hell!

This is the four-player American variant (also referred to as [Oh Pshaw](https://en.wikipedia.org/wiki/Oh_hell#Oh_Pshaw)) with the following modifications:

- There are 13 rounds of hand sizes 1 to 13, with no trump suite for the last hand.
- The bid total must be over or under; someone must lose.
- The default win/loss scoring is as follows (where `x` is the number of tricks hit/missed)
  - Win: `5+x^2`
  - Loss: `5*sum(x)`

Score table:

| Hit | Score | Miss | Score |
| --- | ----- | ---- | ----- |
| 0   | 5     |      |       |
| 1   | 6     | 1    | -5    |
| 2   | 9     | 2    | -15   |
| 3   | 14    | 3    | -30   |
| 4   | 21    | 4    | -50   |
| ... | ...   | ...  | ...   |

## Usage:

```
% python game.py -h
usage: game.py [-h] [--win-metric WIN_METRIC] [--lose-metric LOSE_METRIC]
               name1 name2 name3 name4

Oh Hell Scoring System

positional arguments:
  name1                 The name of the first player
  name2                 The name of the second player
  name3                 The name of the third player
  name4                 The name of the fourth player

options:
  -h, --help            show this help message and exit
  --win-metric WIN_METRIC
                        How to calculate the winning score. Default 5+x**2
  --lose-metric LOSE_METRIC
                        How to calculate the losing score. Default
                        5*sum(range(x+1))
```

**Example:**

```
% python game.py alice bob charlie david

  ____  __     __ __    ______
 / __ \/ /    / // /__ / / / /
/ /_/ / _ \  / _  / -_) / /_/ 
\____/_//_/ /_//_/\__/_/_(_)  

Configuration:
Winning metric: 5+x**2
Losing metric: 5*sum(range(x+1))

Players:
1. alice
2. bob
3. charlie
4. david
[1-4] Who deals first? 2
=================================== Round 1 ===================================
===== Bidding Phase =====
[0-1] bob        bid: 0
[0-1] charlie    bid: 0
[0-1] david      bid: 0
[0-1] alice      bid: 1
Total bids cannot be equal to the round number, please bid again.
[0-1] bob        bid: 0
[0-1] charlie    bid: 0
[0-1] david      bid: 0
[0-1] alice      bid: 0
===== Trick Phase =====
[0-1] bob        tricks: 0
[0-1] charlie    tricks: 0
[0-1] david      tricks: 0
[0-1] alice      tricks: 1
===== Scoring Phase =====
bob        hit  0 and wins 5
charlie    hit  0 and wins 5
david      hit  0 and wins 5
alice      miss 1 and lose 5
Round 1 scores:
alice     : -5
bob       : 5
charlie   : 5
david     : 5
=================================== Round 2 ===================================
===== Bidding Phase =====
[0-2] charlie    bid:
```