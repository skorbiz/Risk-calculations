# Risk-calculations

Odds based on our special variant of risk. The variant includes
- Dynamic reinforcements (Any battle can be reinforced at any time from both attacker or defender). 
- Defender gets to decide whether to use 1 or 2 defence dice after seeing the attach dice.

```
❯ python3 risk.py
Data as losses for defender
attack_roll | n_rolls | probability of roll | accumulated_probability | lose against i dice | 0 loses | 1 loses | 2 loses v | rolls 
----------- | ------- | ------------------- | ----------------------- | ------------------- | ------- | ------- | --------- | ------
(1, 1)      |       1 |                 0.5 |                     0.5 |                 0.0 |   100.0 |     0.0 |       0.0 |
(1, 2)      |       3 |                 1.4 |                     1.9 |                16.7 |    97.2 |     2.8 |       0.0 |
(1, 3)      |       3 |                 1.4 |                     3.2 |                33.3 |    88.9 |    11.1 |       0.0 |
(1, 4)      |       3 |                 1.4 |                     4.6 |                50.0 |    75.0 |    25.0 |       0.0 |
(1, 5)      |       3 |                 1.4 |                     6.0 |                66.7 |    55.6 |    44.4 |       0.0 |
(1, 6)      |       3 |                 1.4 |                     7.4 |                83.3 |    30.6 |    69.4 |       0.0 |
(2, 2)      |       4 |                 1.9 |                     9.3 |                16.7 |    69.4 |    27.8 |       2.8 |
(2, 3)      |       9 |                 4.2 |                    13.4 |                33.3 |    66.7 |    25.0 |       8.3 |
(3, 3)      |       7 |                 3.2 |                    16.7 |                33.3 |    44.4 |    44.4 |      11.1 |
(2, 4)      |       9 |                 4.2 |                    20.8 |                50.0 |    58.3 |    27.8 |      13.9 |
(2, 5)      |       9 |                 4.2 |                    25.0 |                66.7 |    44.4 |    36.1 |      19.4 |
(3, 4)      |      15 |                 6.9 |                    31.9 |                50.0 |    41.7 |    36.1 |      22.2 |
(2, 6)      |       9 |                 4.2 |                    36.1 |                83.3 |    25.0 |    50.0 |      25.0 |
(4, 4)      |      10 |                 4.6 |                    40.7 |                50.0 |    25.0 |    50.0 |      25.0 |
(3, 5)      |      15 |                 6.9 |                    47.7 |                66.7 |    33.3 |    33.3 |      33.3 |
(3, 6)      |      15 |                 6.9 |                    54.6 |                83.3 |    19.4 |    36.1 |      44.4 |
(4, 5)      |      21 |                 9.7 |                    64.4 |                66.7 |    22.2 |    36.1 |      41.7 |
(5, 5)      |      13 |                 6.0 |                    70.4 |                66.7 |    11.1 |    44.4 |      44.4 |
(4, 6)      |      21 |                 9.7 |                    80.1 |                83.3 |    13.9 |    27.8 |      58.3 |
(5, 6)      |      27 |                12.5 |                    92.6 |                83.3 |     8.3 |    25.0 |      66.7 |
(6, 6)      |      16 |                 7.4 |                   100.0 |                83.3 |     2.8 |    27.8 |      69.4 |
```

