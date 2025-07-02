# RPG-Game
Created a turn-based RPG-style game using Tkinter and Python

Week 7 of learning Python. I decided to take a break from CS50P and apply the skills I had learned in a practical project. The code for the game is located in the file RPG.py.

This is the main menu of the game. I am using the Tkinter library to display a frame for the menu. I also used the PIL library for the Image and to resize it. I then used a label to cover the background. 
The start button on the main menu will stop displaying the current frame and immediately put you into the game with a randomly chosen class and monster to fight

![image](https://github.com/user-attachments/assets/69d5da06-4f3f-432d-9eb9-4c2f47ce0f6a)

Here is an example of what happens when you click the start button

![image](https://github.com/user-attachments/assets/025d13b5-7069-4ccd-a168-e492b8a2f179)

Here is an example of what happens when you click the class button

This is how the game looks when playing 

![image](https://github.com/user-attachments/assets/37877d7b-b09c-42ab-90f0-0d32a3457eec)

We win

![image](https://github.com/user-attachments/assets/5dfa4b93-f6a2-452f-ab59-1c484f6518d8)

This is the code used to create the buttons

![image](https://github.com/user-attachments/assets/182455c7-11f8-467c-a5fd-710f26a70b41)

The functions class_menu and start_game are used to provide functionality to the buttons

![image](https://github.com/user-attachments/assets/42c0f33b-eeb9-406f-8b29-e0323f5f0d00)

![image](https://github.com/user-attachments/assets/b1176768-7a5f-46ad-8fdb-4e996f905844)

In this menu, you are presented with 3 different hero classes. I am using mouse events in Tkinter to detect if a player clicks on the select class or not.

The code used to create this menu is below. 

To briefly explain, each class has its own Frame. This allows me to easily separate the parent frame into 3 sections. In each frame, I am creating a canvas.
The Canvas class from Tkinter allows me to create an object that lets me create images, shapes, and more. I also used Pillow, a Python library for manipulating image,s to
Resize and open each image before applying it to the Tkinter canvas. To create the mouse events I used a method called bind that checks for an event such a button click and runs a function when that event
occurs.

![image](https://github.com/user-attachments/assets/e0354be3-fef2-473d-be6b-94c5a122624f)

The functions used to begin the game after a mouse event has been detected. 

The code below creates either a Knight, Wizard or Archer object, which is instantiated from their designated player classes. I then use the random module to select either a Goblin, Skeleton or Dragon.
When a selection is made for the monster, an object will created associated with the monster class. Then I unpack the current frame and start the game.

![image](https://github.com/user-attachments/assets/86b6f416-da15-4518-802c-dba248b8f447)

Character Class

![image](https://github.com/user-attachments/assets/f84baa02-e331-46d5-9ddb-fcb7d108fbdd)

This code is used to provide the values that for each attribute to construct the character class object.

![image](https://github.com/user-attachments/assets/53580ad1-ded7-4d6e-8e49-03c8d3efd278)

Monster Class 

![image](https://github.com/user-attachments/assets/ef7a839d-e29c-487c-8960-f90968581c10)

![image](https://github.com/user-attachments/assets/3212af6d-239f-4a07-9db4-6b65fa3be062)

GameUI class, this is the class where the actual gameplay occurs. In this code I am creating a window, a frame, and using the monster and player objects and storing them as instance variables used
in the class.

![image](https://github.com/user-attachments/assets/440d5e33-1705-4836-9c51-1a6b5474a967)

The code below I am creating individual frames for the player, monster, log messages and buttons. I am also creating a canvas object that allows me to create images, shapes, healthbars and more. Each button also has a function associated with it.

![image](https://github.com/user-attachments/assets/ef733761-4734-4214-b5a3-4dcc231aad66)

Here's how the game looks when running

![image](https://github.com/user-attachments/assets/ec1380b8-b05b-4a55-9d18-25f099efd466)

As you can see my game has multiple abilities, monsters and different types of classes you can play as. Abilities refresh every 4 turns and monsters also have unique abilities that happen at random.

Function used for players ability

![image](https://github.com/user-attachments/assets/f1fa5c51-a92a-4e4c-994e-3dd5ba49c69b)

![image](https://github.com/user-attachments/assets/a21ecb12-aae2-4fa1-8a4b-16d6d3b175dc)

This is the code used to create the player and monster when the game starts

![image](https://github.com/user-attachments/assets/80c25ab7-60ec-43ed-b50c-2233d6672ae5)

This is the combat system of the game. 

![image](https://github.com/user-attachments/assets/d9192d2b-1bcb-4345-9dd6-e26299789b59)

Each monsters unique abilities, I have created functions for all of them

![image](https://github.com/user-attachments/assets/a53ebe95-47c4-4255-bb74-2bae6b263796)

Function used when monster is attacking

![image](https://github.com/user-attachments/assets/079ee96d-dbbe-4f36-8899-b7ebfb089f46)

Function used when player is attacking

![image](https://github.com/user-attachments/assets/12dfe013-ebee-4fb2-9d02-66920e360cb1)

Function used for buff button and heal. I also have a working health bar

![image](https://github.com/user-attachments/assets/deb69668-ad56-4320-a0dc-76e5e7d0f874)

















