![Main Menu](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/GUI/main%20menu%20screen.png)

Deception-based Fighting Game. Two Psychics slug it out!! 

# Game description

Psychic Fighters is a two player game of deception. The goal is to outsmart your opponent with feints. The game is played in turns, with one player being an attacker and the other player being the defender.

# About

This is my first global game jam game I've ever created. Its called Psychic Fighters.

The theme for 2010 is "Deception". We've decided to make a game where the players are "psychic" and can sense their opponent's attack.

# The Global Game Jam 2010 team

![Team Pic](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/GUI/TeamPic.JPG)

## Code

This is the first time I made a non-demo game in python and pygame. Frankly, I am quite embarrased by my code. But everyone have to start somewhere.

The most embarrasing thing I've done is mix spaces and tabs. Well, it worked on python 2.6, so I didn't noticed until I needed to show off the game and it didn't work on newer python versions.

## Art

The art was done by Tien, who I collaborated with at the jam.

## Internal Playtester

Ivanwafoo was a student at the time who wanted to learn how to develop games. He served as our playtester during development.

# How to run

1. To play, first download or clone the game from Github.
2. Download Python (preferably Python 3.4+). Either put the python executable in your path or include the path when running the shell commands
3. Change directory to the game. If you downloaded as a zip file, unzip first.
4. Open your shell/terminal and run the following: *pip install requirements.txt*
5. Run the game: *python main.py*

# How to play

The game is played by two players (there's no AI). Controls for Overhead and Uppercut are as follows: Player 1 - W and D; Player 2 - Up and Down.

Each player have two turns where they are attacking and defending. For each successful offense, the attacker gets 100 points. For each successful block, the defender gets 30 points.

![Visual shadows](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/cutscene/tutorial4_a.png)

The twist here is that the defender will sense (in a form of a visual shadow) if the attacker is planing to use their overhead or their uppercut. This allows the defender to block properly. But the attacker can change their offense at any point before their attack starts. The key is to trick the defender into blocking wrong.

# The characters

## Mister Muscleman

![Muscleman attack animation](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/muscleman/muscleman-attack.gif)

Psychic Boxer with a heart of gold. Very naive.

His ending is typical of fighting game comedy endings and we are shown that the final boss is incompetent in the basics of using psychic fighting.

Only available as player 1 because of game jam constraints

## Spark Plug

![Spark Plug attack animation](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/slimdude/slimdude-attack2.gif)

Technological whiz kid who is somehow using precognition to gain knowledge of his enemies.

His ending is typical of fighting game serious endings and is an obvious Matrix rip-off.

Only available as player 2 because of game jam constraints

## Agent I

![Agent I](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/cutscene/muscleman%20fight%20scene%20with%20AI.png)

The final boss of the game (non playable).

## Everyone else
![Character select](https://raw.githubusercontent.com/MrValdez/ggj2010-Psychic-Fighters/master/GUI/character%20select.png)

Characters that we would have implemented if we built this into a real game.

# Tips
1. If you have good reaction you can see the attack coming.
2. Mash to win.
3. One of our players recommended this as a drinking game. We don't but ymmv.
4. To win, you have to get more points than your opponent.

# Original Global Game Jam 2010 entry
[http://globalgamejam.org/2010/psychic-fighters](http://globalgamejam.org/2010/psychic-fighters)

# My blog posts

1. [On the experience of doing a game jam](https://mrvaldez.ph/global-game-jam-2010-my-experience)
1. [Programming the game](https://mrvaldez.ph/global-game-jam-2010-programming)

# License
This project is licensed under the MIT License - see the LICENSE file for details