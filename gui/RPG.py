from tkinter import *
from PIL import Image, ImageTk
import random
import time
import messages
from messages import strength_buff_msgs_wizard
from messages import strength_buff_msgs_archer
from messages import strength_buff_msgs_knight
import pygame

pygame.init() #initialized pygame
pygame.mixer.init() #intitalized the audio system

pygame.mixer.music.load(r"C:\Users\Faizan\Desktop\classes\gui\rpgmusic.mp3") #loads mp3 file 
pygame.mixer.music.play(-1) #plays mp3 file in a loop


class Menu:
    def __init__(self, window_menu):
        self.window_menu = window_menu
        self.window_menu.geometry("700x400")
        self.window_menu.configure(bg="green")
        self.window_menu.title("Dungeon Defender")
        
        self.bg_image = Image.open(r"C:\Users\Faizan\Desktop\classes\gui\Menu.png")
        self.bg_image = self.bg_image.resize((700,400))
        self.after_image = ImageTk.PhotoImage(self.bg_image)
        self.label = Label(self.window_menu, image=self.after_image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = Frame(self.window_menu,bg="", highlightthickness=0, bd=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        
        self.button_menu = Button(
            self.window_menu,
            text="START",
            font=("Helvetica", 16, "bold"),
            bg="#8B0000",       # Dark red
            fg="white",
            activebackground="#a52a2a",
            relief=FLAT,
            bd=0,
            command=self.start_game
        )
        self.button_classes = Button(
            self.window_menu,
            text="CLASSES",
            font=("Helvetica", 16, "bold"),
            bg="#8B0000",       # Dark red
            fg="white",
            activebackground="#a52a2a",
            relief=FLAT,
            bd=0,
            command=self.class_menu
        )

        self.button_classes.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.button_menu.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    def class_menu(self):
        self.frame.pack_forget()
        menu_class = MenuCharacters(self.window_menu, self)

    def start_game_via_class_select(self, player, monster):
        game2 = GameUI(self.window_menu, player, monster)
        

    def start_game(self):
        player_random = random.choice([Knight, Wizard, Archer])
        player = player_random()
        random_monster = random.choice([Goblin, Skeleton,Dragon])
        monster = random_monster()
        self.frame.pack_forget()
       
        game = GameUI(self.window_menu, player, monster)

class MenuCharacters:
    def __init__(self, window, menu_instance):
        self.window_class_menu = window
        self.menu = menu_instance
        self.frame = Frame(self.window_class_menu, width=700, height=400, bg="#1e1e1e")
        self.frame.pack(fill=BOTH)

        self.frame_knight = Frame(self.frame, width=233, height=400, bg="#2e2b2b")
        self.frame_knight.pack(side=LEFT, pady=10, padx=10)

        self.knight_image = Image.open(r"C:\Users\Faizan\Desktop\classes\gui\Knight.png")
        self.knight_image = self.knight_image.resize((220,300))
        self.knight_image_selector = ImageTk.PhotoImage(self.knight_image)

        self.knight_canvas = Canvas(self.frame_knight, width=223, height=400, bg="#1e1e1e")
        self.knight_canvas.image = self.knight_image_selector
        self.knight_canvas.pack()
        self.knight_canvas.create_image(5,30, image=self.knight_image_selector, anchor=NW)
       
        self.frame_wizard = Frame(self.frame, width=233, height=400, bg="#1e1e1e")
        self.frame_wizard.pack(side=LEFT, pady=10, padx=10)
        self.wizard_image = Image.open(r"C:\Users\Faizan\Desktop\classes\gui\Wizard.png")
        self.wizard_image = self.wizard_image.resize((220,300))
        self.wizard_image = ImageTk.PhotoImage(self.wizard_image)

        self.wizard_canvas = Canvas(self.frame_wizard, width=223, height=400, bg="#1e1e1e")
        self.wizard_canvas.image = self.wizard_image
        self.wizard_canvas.pack()
        self.wizard_canvas.create_image(0,35, image=self.wizard_image, anchor=NW)

        self.frame_archer = Frame(self.frame, width=233, height=400, bg="#1e1e1e")
        self.frame_archer.pack(side=RIGHT, padx=10, pady=10)

        self.archer_image = Image.open(r"C:\Users\Faizan\Desktop\classes\gui\Archer.png")
        self.archer_image = self.archer_image.resize((220,300))
        self.archer_image = ImageTk.PhotoImage(self.archer_image)
        
        self.archer_canvas = Canvas(self.frame_archer, width=223, height=400, bg="#1e1e1e")
        self.archer_canvas.image = self.archer_image
        self.archer_canvas.pack()
        self.archer_canvas.create_image(-15,35, image=self.archer_image, anchor=NW)

        self.knight_canvas.bind("<Button-1>",self.select_knight)
        self.wizard_canvas.bind("<Button-1>",self.select_wizard)
        self.archer_canvas.bind("<Button-1>", self.select_archer)


    def select_knight(self, event): 
        player = Knight()
        random_monster = random.choice([Goblin,Skeleton, Dragon])
        monster = random_monster()
        self.frame.pack_forget()
        self.menu.start_game_via_class_select(player, monster)
    
    def select_wizard(self, event):
        player = Wizard()
        random_monster = random.choice([Goblin, Skeleton, Dragon])
        monster = random_monster()
        self.frame.pack_forget()
        self.menu.start_game_via_class_select(player, monster)

    def select_archer(self, event):
        player = Archer()
        random_monster = random.choice([Goblin, Skeleton, Dragon])
        monster = random_monster()
        self.frame.pack_forget()
        self.menu.start_game_via_class_select(player, monster)

    
class Character:
    def __init__(self, name, max_health, damage, original_damage, attack_chance, ability, sprite_path, attack_audio, ability_audio, button_text, button2_text, button3_text, button4_text, player_critical_dmg, player_critical_chance):
        self.name = name
        self.max_health = max_health
        self.damage = damage
        self.health = max_health
        self.sprite_path = sprite_path
        self.attack_chance = attack_chance
        self.ability = ability
        self.buff = False
        self.attack_audio = attack_audio
        self.ability_audio = ability_audio
        self.button_text = button_text
        self.button2_text = button2_text
        self.button3_text = button3_text
        self.button4_text = button4_text
        self.player_critical_chance = player_critical_chance
        self.player_critical_dmg = player_critical_dmg
        self.original_damage = original_damage
        

    def take_damage(self, damage_amount):
        self.max_health -= damage_amount
        return self.max_health
    
    def heal(self, amount):
        self.health += amount
        self.health = min(self.health, self.max_health)

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True
    
class Knight(Character):
    def __init__(self):
        super().__init__("Knight", 300, 40, 40, [1,3,4,5,6,8,9], "shield", r"C:\Users\Faizan\Desktop\classes\gui\Knight.png", r"C:\Users\Faizan\Desktop\classes\gui\sword.wav", r"C:\Users\Faizan\Desktop\classes\gui\slash.wav", "STRIKE", "DEFENSE", "OVERCHARGE", "NULLIFY", 2, [1,9,6,7,8])
        self.nullify = False
        self.secondary_audio_ability_knight = r"C:\Users\Faizan\Desktop\classes\gui\nullify.wav"
class Wizard(Character):
     def __init__(self):
         super().__init__("Wizard", 180, 80, 80,[1,3,4,5,6,7], "fireball", r"C:\Users\Faizan\Desktop\classes\gui\Wizard.png", r"C:\Users\Faizan\Desktop\classes\gui\fireballsound.wav", r"C:\Users\Faizan\Desktop\classes\gui\fireballs.wav", "BLAST", "CONJURE", "UNLEASH", "CURSE", 3, [1,2])
         self.curse = False
         self.secondary_audio_ability_wizard = r"C:\Users\Faizan\Desktop\classes\gui\curse.wav"
class Archer(Character):
    def __init__(self):
        super().__init__("Archer", 230, 70, 70, [1,3,4,8,9,5], "blinded", r"C:\Users\Faizan\Desktop\classes\gui\Archer.png", r"C:\Users\Faizan\Desktop\classes\gui\arrow.wav", r"C:\Users\Faizan\Desktop\classes\gui\arrowdraw.wav", "SHOOT", "PIERCE", "BLIND", "INFUSE", 3, [1,3,4,5,6,7,8])
        self.secondary_audio_ability_archer = r"C:\Users\Faizan\Desktop\classes\gui\archerdraw.wav"
class Monster:
    def __init__(self, name, damage, max_health, attack_chance, sprite_path):
        self.max_health = max_health
        self.damage = damage
        self.name = name
        self.health = max_health
        self.sprite_path = sprite_path
        self.attack_chance = attack_chance

    def take_damage(self, damage_amount):
        self.damage_amount = damage_amount
        self.health -= self.damage_amount
        return self.health

    def is_alive(self):
         if self.health <= 0:
            return False
         else:
            return True

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 25, 150, [1,3,2,5,6,8], r"C:\Users\Faizan\Desktop\classes\gui\goblin.png")
        self.ability_stab = False

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 53, 600, [1,6,3,2,4], r"C:\Users\Faizan\Desktop\classes\gui\Skeleton.png")
        self.ability_weak = False
        self.ability_poison = False
class Dragon(Monster):
    def __init__(self):
        super().__init__("Dragon", 56, 480, [3,7,5,6,1], r"C:\Users\Faizan\Desktop\classes\gui\Dargon.png")

class GameUI:
    def __init__(self, window, character, monster):
        #Window for game
        self.window = window
        self.window.title("Dungeon Defender")
        self.window.geometry("700x400")
        self.window.configure(bg="#1e1e1e")
        self.turn = 1
        self.count_click = 0
        self.frame = Frame(self.window, bg="#1e1e1e")
        self.frame.pack(fill=BOTH, expand=True)
        #Define monster
        self.monster = monster
        #Define Character
        self.player = character
    
        #Player Frame
        self.left = Frame(self.frame, bg="#1e1e1e", height=600, width=200)
        self.left.pack(side=LEFT, anchor="w", fill=Y)
        
        #Player Health Bar
        self.health_canvas = Canvas(self.left, width=30, height=20, highlightthickness=0, bg="red")
        self.health_canvas.pack(padx=10, fill=X)
        
        #Player rectangle health bar
        self.player_health_rect = self.health_canvas.create_rectangle(0,0,200,30,fill="green")
        
        #Monster Frame
        self.right = Frame(self.frame, bg="#1e1e1e", height=600, width=200)
        self.right.pack(side=RIGHT, anchor="e", fill=Y)

        #Monster Health Bar
        self.health_monster_canvas = Canvas(self.right, width=30, height=20, highlightthickness=0, bg="red")
        self.health_monster_canvas.pack(padx=10, fill=X)

        #Monster rectangle health bar
        self.monster_health_rect = self.health_monster_canvas.create_rectangle(0, 0, 200, 100, fill="green")
        
        #Attack, Heal, Buff Frame
        self.button_area = Frame(self.frame, bg="#1e1e1e", height=100, width=300)
        self.button_area.pack(side=BOTTOM, anchor="s", fill=X)
        
        #Log Messages
        self.actual_logs = Frame(self.frame, bg="#1e1e1e", height=100, width=200)
        self.actual_logs.pack(side=TOP, anchor="n", fill=X)

        #Attack Button
        self.button = Button(self.button_area, text=self.player.button_text, width=10, command=self.combat, bg="#8b0000", fg="#f5f5f5", relief=RAISED, bd=2, activebackground="#650909")
        self.button.grid(row=1, column=0, padx=10, pady=10)

        #Heal Butto
        self.button_heal = Button(self.button_area, text="HEAL", width=10, fg="#f5f5f5", bg="#006400", relief=RAISED, bd=2, activebackground="#093509", command=self.heal)
        self.button_heal.grid(row=1,column=1, padx=10, pady=10)

        #Strength Button
        self.strength_buff_button = Button(self.button_area, text=self.player.button2_text, width=10, bg="#1e90ff", fg="#f5f5f5", relief=RAISED, bd=2, activebackground="#1f5d9b", command=self.strength_buff)
        self.strength_buff_button.grid(row=1,column=2, padx=2, pady=10)

        #Inventory Button
        self.inventory_button = Button(self.button_area, text="INVENTORY", width=10, bg="#bc1c1c", fg="#f5f5f5", relief=RAISED, bd=2, activebackground="#650909")
        self.inventory_button.grid(row=2, column=0, padx=10, pady=10)

        self.hero = Button(self.button_area, text=self.player.button3_text, width=10, bg="#1e90ff", relief=RAISED, bd=2, activebackground="#1f5d9b", fg="#f5f5f5", command=self.unique_ability)
        self.hero.grid(row=2, column=1, padx=10, pady=10)

        self.secondability = Button(self.button_area, text=self.player.button4_text, command=self.secondary_ability, width=10, bg="#1e90ff", fg="#f5f5f5", relief=RAISED, bd=2, activebackground="#093509")
        self.secondability.grid(row=2, column=2, padx=10, pady=10)

        #Text area for logs
        self.text = Text(self.actual_logs, width=20, height=15, bg="#1e1e1e", font=("Ink Free",10), fg="#f5f5f5")
        self.text.pack(fill=X)

        #Create Player
        self.create_player()
        
        #Create Monster
        self.create_monster()
    
    def secondary_ability(self):
        if self.player.name == "Archer":
            audio = pygame.mixer.Sound(self.player.secondary_audio_ability_archer)
            audio.play()
            self.player.damage *= 2
            self.text.insert("1.0","You notch a glowing arrow and let it fly with deadly precision — your next strike will deal double damage!")
            self.secondability["state"] = DISABLED
        elif self.player.name == "Knight":
            audio = pygame.mixer.Sound(self.player.secondary_audio_ability_knight)
            audio.play()
            self.text.insert("1.0", "🛡️ *Iron Wall!* The Knight raises his shield with unwavering resolve — all incoming damage will be nullified this turn!\n\n")
            self.secondability["state"] = DISABLED
        else:
            audio = pygame.mixer.Sound(self.player.secondary_audio_ability_wizard)
            audio.play()
            self.text.insert("1.0", "🧙‍♂️ *Dark Hex!* You whisper forbidden words, and a shadowy curse wraps around the enemy — their strength begins to wither!\n\n")
            self.monster.health -= 10
            self.player.curse = True
            self.secondability["state"] = DISABLED

        
    def unique_ability(self):
        audio = pygame.mixer.Sound(self.player.attack_audio)
        if self.player.name == "Archer":
            audio.play()
            self.text.insert("1.0", "🏹 Your arrow strikes true! You blinded the enemy with your precision shot — their vision fades!\n\n")
            self.monster.attack_chance = [1,2]
            self.hero["state"] = DISABLED
        elif self.player.name == "Knight":
            audio.play()
            print("knight")
            self.player.nullify = True
            
            self.text.insert("1.0", "🛡️ Knight braces for impact! Your defense ability activates — incoming damage is reduced.\n\n")
            self.hero["state"] = DISABLED
        else:
            audio.play()
            self.player.damage += 300
            print(self.player.damage)
            self.player.health = 80
            self.bar_width_player = round((self.player.health / self.player.max_health)*200)
            self.health_canvas.coords(self.player_health_rect,0,0,self.bar_width_player,100)
            self.text.insert("1.0", "🔥 *Fireball Unleashed!* You conjure a blazing fireball and hurl it at the enemy, your body weakens \n\n")
            self.hero["state"] = DISABLED
    def create_player(self):
        #Creates canvas for player frame
        self.canvas = Canvas(self.left, width=200, height=600, bg="#1e1e1e")

        #Open image using PIL
        self.big_image = Image.open(self.player.sprite_path)

        #Resize Image with PIL
        self.resized_image = self.big_image.resize((200, 400))
        
        #Create photo image with ImageTK.PhotoImage. 
        self.photo_image = ImageTk.PhotoImage(self.resized_image)

        #Create Image and positions it to left side of frame
        self.canvas.create_image(0, 0, image=self.photo_image, anchor=NW)
        
        self.canvas.pack(side=LEFT, anchor="n", fill=Y)

    def create_monster(self):
        #Create canvas for monster frame
        self.canvas_monster = Canvas(self.right, width=200, height=600, bg="#1e1e1e")

        #open image and store it variable
        self.big_image_monster = Image.open(self.monster.sprite_path)

        #Resize monster image
        self.resized_image_monster = self.big_image_monster.resize((200,400))

        #create photo image
        self.actual_image_monster = ImageTk.PhotoImage(self.resized_image_monster)

        self.canvas_monster.image = self.actual_image_monster

        #Create the actual image
        self.canvas_monster.create_image(0,0, image=self.actual_image_monster, anchor=NW)

        #Places image to right side of frame
        self.canvas_monster.pack(side=RIGHT, anchor="e", fill=Y)
        
    def combat(self):
        if self.turn % 2 == 0:
            self.turn +=1
        else:
            if not self.player.is_alive():
                self.text.insert("1.0", f"{self.player.name} DIED")
                self.button["state"] = DISABLED
                self.strength_buff_button["state"] = DISABLED
                self.button_heal["state"] = DISABLED
                self.hero["state"] = DISABLED
                self.secondability["state"] = DISABLED
                self.text.insert("1.0",f"👹 The monster kills you!\n\n")
                self.window.after(6000, self.back_to_main_menu)
                return ""
            
            self.turn +=1
            self.attack()
            if not self.monster.is_alive():
                self.text.insert("1.0", f"{self.monster.name} SLAINED +3 GOLD")
                self.button["state"] = DISABLED
                self.strength_buff_button["state"] = DISABLED
                self.button_heal["state"] = DISABLED
                self.window.after(6000, self.back_to_main_menu)
                return ""

    
            self.text.update()
            self.window.after(1500, self.text.insert("1.0", "Monster is thinking\n\n"))
            self.window.after(3000, self.attack_monster)

    def back_to_main_menu(self):
        self.frame.destroy()
        Menu(self.window)
    
    def dragon_breath(self):
        damage = random.choice([80,90,33,113,21,200])
        self.player.health -= damage
        self.bar_width_player = round((self.player.health / self.player.max_health)*200)
        self.health_canvas.coords(self.player_health_rect,0,0,self.bar_width_player,100)
        self.text.insert("1.0", f"You’re caught in the Dragon’s blazing breath! HP remaining {self.player.health}\n\n")
    def dragon_burn(self):
        damage = random.choice([10,20,30])
        self.player.health -= damage
        self.bar_width_player = round((self.player.health / self.player.max_health)*200)
        self.health_canvas.coords(self.player_health_rect,0,0,self.bar_width_player,100)
        self.text.insert("1.0", f"The dragon burns your skin, you are unable to your abilities. HP remaining {self.player.health}\n\n")
        self.hero["state"] = DISABLED
        self.secondability["state"] = DISABLED

    def goblin_eye_slash(self):
        self.player.attack_chance = [1,2]
        self.player.health -= 50
        self.text.insert("1.0", f"🗡️ The Goblin leaps wildly and slashes at your eyes. Your accuracy has dropped dramatically\n\n")
        self.bar_width_player = round((self.player.health / self.player.max_health)*200)
        self.health_canvas.coords(self.player_health_rect,0,0,self.bar_width_player,100)
        self.monster.ability_stab == True
    
    def weaken(self):
        self.player.damage -= 20
        self.text.insert("1.0", "🦴The air chills as the Skeleton Lord chants in a forgotten tongue — your power begins to fade..\n\n")
        self.monster.ability_weak = True

    def poison(self):
        self.player.health -= 10
        self.text.insert("1.0", f"The Skeleton lord casts a nasty spell, engulfing you in a myst of poison - HP remaining {self.player.health}\n\n")
        self.monster.ability_poison = True
    def attack_monster(self):
        number_monster_random = random.randint(1,10)
        if hasattr(self.player, "curse") and self.player.curse:
            self.monster.health -= 30
            self.text.insert("1.0", f"💥 The curse pulses with dark energy — the monster winces as it suffers 10 damage. Monster HP {self.monster.health}\n\n")
            bar_width = round((self.monster.health / self.monster.max_health) * 200)
            self.health_monster_canvas.coords(self.monster_health_rect,0,0,bar_width,100)
        if hasattr(self.player, "nullify") and self.player.nullify:
            self.text.insert("1.0", f"🛡️ {self.player.name} blocks all damage with Iron Wall!\n\n")
            self.player.nullify = False
            return ""
        elif number_monster_random == 4 and self.monster.name == "Dragon":
            self.dragon_breath()
            return ""
        elif number_monster_random == 9 and self.monster.name == "Dragon":
            self.dragon_burn()
            return ""
        elif number_monster_random in [1,9] and self.monster.name == "Goblin" and self.monster.ability_stab == False:
            self.goblin_eye_slash()
            return "" 
        elif number_monster_random == 6 and self.monster.name == "Skeleton" and self.monster.ability_weak == False:
            self.weaken()
            return "" 
        elif number_monster_random == 8 and self.monster.name == "Skeleton" and self.monster.ability_poison == False:
            self.poison()
            return "" 

        elif number_monster_random in self.monster.attack_chance:
            
            #if monster is able to strike, reduce player health
            self.player.health -= self.monster.damage
            #Update player health bar when damage is taken
            self.bar_width_player = round((self.player.health / self.player.max_health)*200)
            self.health_canvas.coords(self.player_health_rect,0,0,self.bar_width_player,100)
            
            self.text.insert("1.0",f"> The monster claws at you! ❤️ Your HP remains at: {self.player.health}\n\n")
    #Checks if monster misses strike
        else:
            if self.monster.name == "Dragon":
                self.text.insert("1.0", f"{messages.dragon()}\n\n")
            elif self.monster.name == "Goblin":
                self.text.insert("1.0", f"{messages.goblin_messages__miss()}")
            else:
                self.text.insert("1.0", f"{messages.skeleton_messages_miss()}")


        #Turn based combat
        
        
        #AI should have randomized abilities
    def attack(self):
        audio = pygame.mixer.Sound(self.player.ability_audio)
        audio.play()
        
        
        self.count_click += 1
        if self.count_click in range(4,1000,4):
            self.secondability["state"] = NORMAL
            self.hero["state"] = NORMAL
            self.strength_buff_button["state"] = NORMAL
        #Picks a number between 1 and 10 to determine randomness of strikes
        number_player_random = random.randint(1,10)
        
        #Player attack strength stored in local variable
       
        if number_player_random in self.player.attack_chance:
        #Checks if monster health is 0. Buttons will be disabled and Goblin is slained
            #if player strikes, reduce monster health by attack strength
            self.monster.health -= self.player.damage
            #Check if attack is 50, since buff is one time
            #Insert text in log messages    
            self.text.update()

            self.window.after(200, self.text.insert("1.0",f"⚔️ You strike the monster for {self.player.damage} damage! Its HP drops to {self.monster.health}.\n\n"))
            if self.player.damage == 140:
                self.player.damage /= 2
            elif self.player.damage == 380:
                self.player.damage -= 300
           
            #Update bar health depending on damage done to monster
            bar_width = round((self.monster.health / self.monster.max_health) * 200)
            self.health_monster_canvas.coords(self.monster_health_rect,0,0,bar_width,100)

            if hasattr(self.player, "buff") and self.player.buff:
                self.player.damage -= 30
                self.player.buff = False
            
            if self.player.damage == 300:
                self.player.damage -= 300
        else:
            if self.player.name == "Knight":
                self.text.insert("1.0",messages.knight_messages_miss())
            elif self.player.name == "Archer":
                self.text.insert("1.0", messages.archer_messages_miss())
            else:
                self.text.insert("1.0", messages.wizard_messages_miss())
        self.combat()

    def strength_buff(self):
        #Upgrade attack by 30
        audio = pygame.mixer.Sound(r"C:\Users\Faizan\Desktop\classes\gui\power up.wav")
        audio.play()
        if self.player.name == "Knight":
            self.text.insert("1.0", f"{strength_buff_msgs_knight()}")
        elif self.player.name == "Archer":
            self.text.insert("1.0", f"{strength_buff_msgs_archer()}")
        elif self.player.name == "Wizard":
            self.text.insert("1.0", f"{strength_buff_msgs_wizard()}")
        self.player.damage += 30
        self.player.buff = True
        #change button state to disable after activating it
        self.strength_buff_button["state"] = DISABLED

    def heal(self):
        #Increase health by 50
        self.player.health += 50
        sound = pygame.mixer.Sound(r"C:\Users\Faizan\Desktop\classes\gui\heal.wav")
        sound.play()
        max_health = min(self.player.health, 100)
        #Increase bar width 
        bar_width = round((self.player.health / self.player.max_health) * 200)
        #change coordinates for rectangle to increase health
        self.health_canvas.coords(self.player_health_rect,0,0,bar_width,100)
        #change state from Active to Disabled
        self.button_heal["state"] = DISABLED
        #Increase player health
        self.text.insert("1.0", f"💖 A warm light surrounds you... You regain 50 HP. Current HP: {self.player.health}.\n\n")
         
def main():
    window = Tk()
    window_menu = Menu(window)
    window.mainloop()

main()
