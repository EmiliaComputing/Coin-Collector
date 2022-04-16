# Coin Collector 

### Introduction
I decided to create a game for the purpose of entertainment. The target audience is children of my age (12) as I feel this is the type of game they would choose to play and I think they would enjoy a game with multiple levels to challenge them.

In this game, a character has to collect objects that change every level. At the moment, the game has five levels but I am hoping to add more in the future. Starting from the second level, in order to make the game more challenging, the player also has to avoid a green worm that moves in circles, at a random speed, around the screen. 

If the character on the screen touches the obstacle (the green worm), they lose the game and a red end screen appears. However, if the player collects all of the objects without touching the green worm, a door appears which, when touched by the character, changes the background colour to green displaying a message saying “you won”.
 
### Project Goals/Requirements
I wrote this code in Python because I could use the arcade library for the graphics. I felt that this would give an appropriate look to the game and would fit my overall aim of the project. 

I wanted to create a game for my peers that would help them to switch off from school work and have fun. These types of games do not require a lot of thought to play and that is why I feel it is good for this purpose.

My requirements for this game are a character, an obstacle to make the game harder, items for the player to collect, multiple levels as well as a way to end or complete the game. 

### Design
The user interacts with the computer by using arrow keys and WASD keys on the keyboard to move the player across the screen. 

The background colour is called “unmellow yellow” and I used it because I feel that it resembles the sand in a desert and the background story to the game is that the player is stuck on a desert island. The colour green (“bud green”) is used in the background when the player wins, because green represents success. I used the colour red (“firebrick”) for the background of the screen that appears when the player loses because it is the opposite of green and also because red has negative connotations. In the level where the player had to collect the gems, the gems are red because it stands out next to the yellow whilst still being pleasing to the eye.

I used the graphics in Python’s arcade library.

The following pseudocode shows how the levels work:
  FUNCTION setup_level1
    size_of_task = screen_width/80
    coin_list = arcade.SpriteList
    player_list = arcade.SpriteList
    enemy_list = arcade.SpriteList
    player_sprite = “femalePerson_idle.png”
    player_sprite.center_x = screen_width/2
    player_sprite.center_y = screen_height/2
    task = "You are stuck on a desert island and have found 20 locked suitcases. Find the keys."
    Append the player sprite to the player list
    score = 0
  END FUNCTION

  setup_level1

The following pseudocode describes how the player moves:
  MOVEMENT_SPEED = 5
  IF key == arcade.key.up THEN
      player_sprite.change_y = movement_speed
  END IF

  ELSE IF key == arcade.key.down THEN
      player_sprite.change_y = -movement_speed
  END IF

  ELSE IF key == arcade.key.right THEN
     player_sprite.change_x = movement_speed
  END IF

  ELSE IF key == arcade.key.left THEN
     player_sprite.change_x = -movement_speed
  END IF

### Issues during the project and how I resolved them
There was an issue with the pop up screens that appeared once the player had either won or lost. When the game was over, the pop up screens were covered in enemies and items to collect which was not supposed to happen. At the end, it was supposed to be a red end screen with nothing else on it. I resolved this by using a for loop where the enemy, player and items would be removed from the sprite lists. 

There was also an issue with the size of the window not fitting onto smaller screens. I resolved this by importing pyautogui and using it to determine the width and height of the window based on the width and height of the screen of the player. 

Another issue was when a player was using a smaller screen, the character appeared to be moving too quickly across the window and appeared to be too large, likewise when the character was on a larger screen, it appeared too small and looked as if it was moving too slowly across the window. I resolved this by, instead of giving the character a fixed speed, determining the speed and size of the character relative to the size of the screen. This prevents the character from getting from one side of the screen to the other too quickly or slowly and it keeps the size of the character relative to the size of the screen. 

### Testing Phase
I tested this project on my peers in my ICT lesson by asking them to play the game. I explained to them how to move the character and what to do to complete the game.

I received feedback saying that the obstacle changed speed too often and sometimes went too quickly. Therefore, I changed the code for how often the obstacle changed speed to make it less frequent. I also changed the code to make the range of speeds the obstacle could go smaller.

I then tested this project again and received no negative feedback.

### Evaluation
I feel as if this project went well because it has fulfilled my expectations and I feel that it has been successful in accomplishing my goals for the project. I also feel that this project was successful because my target audience has responded positively to the completed project. 

If I were to do this project again I would do the enemy, player and game classes in separate files because then it would have been easier to find and resolve errors. It would have also been easier to improve the game as a whole because it would have been quicker to look through the files I wanted to change separately rather than looking through the project as a whole.

Another change that I would make to the game would be for there to be an instruction screen so that I would not have to explain how to move the character and it would enable anybody to be able to play at any time.
