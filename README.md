# d4_pr3fl0p_b0t_v2
#### Authors: Rihards Belinskis, Kaspars Bregis

#### Last update: April 11th, 2020.

Welcome to d4_pr3fl0p_b0t_v2 - the 2nd version of the r1_pr3fl0p_bot (the online poker preflop bot for 888 poker). The bot detects holecards, analyses position and makes a decision based on a given preflop range and the previous action at the table.

The bot follows the following structure (subject to change).

![](/img/flowchart.png?raw=true)

### The bot is limited to:
* The Pacific Poker (888) software;
* No Limit Hold'em;
* 6-max tables;
* Bottom-right sitting position
* Maximized poker window(-s, if all are cascaded on top, and maximized);
* Third "deck" (see [this image](https://github.com/rihardsbelinskis/d4_pr3fl0p_b0t_v2/img/Deck5.png)) from the 888 Game Settings.

### Update history:
* v0.1 - prototype version w/ main function (b0t.py), card detection, position detection and previous action detection. Also preflop hand ranges have been implemented.
* v0.2 - optimized version of v0.1, yet still requires bug-fixing and testing.

### Bug report:
* v0.1 - previous action detection is incorrect (assumes all previous action has been a "fold" if sitting OOP).

## DISCLAIMER: I am not responsible for the use of d4_pr3fl0p_b0t_v2 at real money tables! Using any kind of 3rd party software in online poker is strictly prohibited and can result in a permanent ban of your account, as well as money confiscation. This software is intended for entertainment purposes only!
