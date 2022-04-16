import arcade
import random
import math
import time
import pyautogui

width, height= pyautogui.size()

SCREEN_WIDTH = width - (width//40)
SCREEN_HEIGHT = height - (height//10)
SCREEN_TITLE = 'Coin Collector'
MOVEMENT_SPEED = SCREEN_WIDTH/316
COIN_SCALE = 0.25
enemy_speed = random.randint(2, 8)
x = 1
a = 2
y = 3


class Enemy(arcade.Sprite):
    def __init__(self, filename, scaling):
        super().__init__(filename, scaling)
        width, height= pyautogui.size()
        self.circle_radius = random.randint((SCREEN_WIDTH//38), (SCREEN_WIDTH//2)-50)
        self.circle_speed = random.uniform(0.05, 0.1)
        self.circle_angle= 0
        self.circle_center_x = SCREEN_WIDTH/2
        self.circle_center_y = SCREEN_HEIGHT/2

        self.count_to_change_speed =0
        
    def update(self):
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y

        self.circle_angle += self.circle_speed

        self.count_to_change_speed+=1
        
        if self.count_to_change_speed>=1250:
            self.circle_radius = random.randint((SCREEN_WIDTH//38), (SCREEN_WIDTH//5))
            self.circle_speed = random.uniform(0.05, 0.08)
            self.count_to_change_speed =0

        if self.count_to_change_speed>=1100:
            print("Worm speed changing soon")

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom > SCREEN_HEIGHT:
            self.top = 0
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT
        if self.right < 0:
            self.right = SCREEN_WIDTH
        if self.left > SCREEN_WIDTH:
            self.left = 0

class Game(arcade.Window):
    def __init__(self,  width, height, title):
        super().__init__(width, height, title)
        self.task = ''

        arcade.set_background_color(arcade.color.UNMELLOW_YELLOW)

    def setup_level1(self):
        self.test_size_of_task = SCREEN_WIDTH//80
        self.coin_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.door_list = arcade.SpriteList()
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png")
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.task = "You are stuck on a desert island and have found 20 locked suitcases. Find the keys."

        self.player_list.append(self.player_sprite)

        self.score = 0

        for coin_number in range(20):
            coin = arcade.Sprite(":resources:images/items/keyYellow.png", COIN_SCALE)
            coin.center_x = random.randint(1, SCREEN_WIDTH)
            coin.center_y = random.randint(1, SCREEN_HEIGHT)
            self.coin_list.append(coin)


    def setup_level2(self):
        for coin_number in range(5):
            coin = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")
            coin.center_x = random.randint(1, SCREEN_WIDTH)
            coin.center_y = random.randint(1, SCREEN_HEIGHT)
            self.coin_list.append(coin)
        self.task = 'There are others stuck there with you, find them. Do not touch the worm that lives on the island.'
        self.enemy_sprite = Enemy(":resources:images/enemies/wormGreen.png", 1)
        self.enemy_sprite.center_x = 500
        self.enemy_sprite.center_y = 300
        self.enemy_list.append(self.enemy_sprite)
        self.time_since_last_firing = 0.0

    def setup_level3(self):
        for coin_number in range(20):
            coin = arcade.Sprite(":resources:images/tiles/waterTop_low.png", 0.25)
            coin.center_x = random.randint(1, SCREEN_WIDTH)
            coin.center_y = random.randint(1, SCREEN_HEIGHT)
            self.coin_list.append(coin)
            self.task = 'You are thirsty. Find water.'

    def setup_level4(self):
        for coin_number in range(25):
            coin = arcade.Sprite(":resources:images/items/gemRed.png", 0.5)
            coin.center_x = random.randint(1, SCREEN_WIDTH)
            coin.center_y = random.randint(1, SCREEN_HEIGHT)
            self.coin_list.append(coin)
            self.task = 'You realise that the island is covered in rare gems. Collect the rubies.'
            
    def setup_level5(self):
        for coin_number in range(20):
            coin = arcade.Sprite(":resources:images/isometric_dungeon/stoneWall_S.png", 0.25)
            coin.center_x = random.randint(1, SCREEN_WIDTH)
            coin.center_y = random.randint(1, SCREEN_HEIGHT)
            self.coin_list.append(coin)
            self.task = 'You are getting cold. Collect materials to build a shelter.'
            
    def end_of_game(self):
        for door in range(1):
            door_bottom = arcade.Sprite(":resources:images/tiles/doorClosed_mid.png")
            door_top = arcade.Sprite(":resources:images/tiles/doorClosed_top.png")
            self.task = 'Enter the shelter you have built to win the game.'
            door_bottom.center_x = SCREEN_WIDTH/2
            door_bottom.center_y = 300
            door_top.center_x = SCREEN_WIDTH/2
            door_top.center_y = 400
            self.door_list.append(door_bottom)
            self.door_list.append(door_top)
             
    def on_draw(self):
        enemy_choise = [x, y, a]
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
        self.enemy_list.draw()
        self.door_list.draw()
        self.score_draw = f"{self.score} items"
        self.test_size_of_task = SCREEN_HEIGHT // 25
        arcade.draw_text(self.task, 2, 0, arcade.color.BLACK, self.test_size_of_task) 
        arcade.draw_text(self.score_draw, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30, arcade.color.BLACK, SCREEN_HEIGHT//50)
        
    def on_update(self, delta_time):
        self.player_list.update()
        self.coin_list.update()
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        self.door_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.door_list)
        self.enemy_list.update()
        for enemy in enemy_hit_list:
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            for enemy in self.enemy_list:
                enemy.remove_from_sprite_lists()
            for player in self.player_list:
                player.remove_from_sprite_lists()
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            self.end_lost()
                        
        for door in self.door_hit_list:
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            for enemy in self.enemy_list:
                enemy.remove_from_sprite_lists()
            for player in self.player_list:
                player.remove_from_sprite_lists()
            for coin in self.coin_list:
                coin.remove_from_sprite_lists()
            self.end_won()
            
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        if self.score == 20 and len(self.coin_list) == 0:
            self.setup_level2()
        elif self.score == 25 and len(self.coin_list) == 0:
            self.setup_level3()
        elif self.score == 45 and len(self.coin_list) == 0:
            self.setup_level4()
        elif self.score == 70 and len(self.coin_list) == 0:
            self.setup_level5()
        elif self.score == 90 and len(self.coin_list) == 0:
            self.end_of_game()

    def on_key_press(self, key, modifiers):
        #Arrow Keys
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

        #WASD Keys
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
            
    def end_lost(self):
        self.test_size_of_task = SCREEN_WIDTH//190
        arcade.set_background_color(arcade.color.FIREBRICK)
        self.task = "YOU LOST"
        for coin in self.coin_list:
            coin.remove_from_sprite_lists()
            if len(self.coin_list) != 0:
                coin.remove_from_sprite_lists()
        for enemy in self.enemy_list:
            enemy.remove_from_sprite_lists()
        for player in self.player_list:
            player.remove_from_sprite_lists()

    def end_won(self):
        self.test_size_of_task = SCREEN_WIDTH//190
        arcade.set_background_color(arcade.color.BUD_GREEN)
        self.task = "YOU WON"
        for coin in self.coin_list:
            coin.remove_from_sprite_lists()
        for enemy in self.enemy_list:
            enemy.remove_from_sprite_lists()
        for player in self.player_list:
            player.remove_from_sprite_lists()
        for door in self.door_hit_list:
            door.remove_from_sprite_lists()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup_level1()
arcade.run()
