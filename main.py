import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self, snake_flag: int):
        if snake_flag == 0:        
            self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
            # self.direction = Vector2(1,0)
        else:
            self.body = [Vector2(5,15), Vector2(4,15), Vector2(3,15)]
            # self.direction = Vector2(1,0)
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

        # self.direction_lock = False

    def draw_snake(self):        
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            # Create a Rect for Positioning            
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)            
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # Determine Directions of Body and Load Graphics
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    if prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    if prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    if prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_direction = self.body[1] - self.body[0]

        if head_direction == Vector2(1, 0):
            self.head = self.head_left
        elif head_direction == Vector2(-1, 0):
            self.head = self.head_right
        elif head_direction == Vector2(0, 1):
            self.head = self.head_up
        else:
            self.head = self.head_down     

    def update_tail_graphics(self):
        tail_direction = self.body[-2] - self.body[-1]

        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_direction == Vector2(0, 1):
            self.tail = self.tail_up
        else:
            self.tail = self.tail_down

    def move_snake(self):       # REVIEW
        if self.new_block == True:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]

        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self, snake_flag: int):
        if snake_flag == 0:            
            # Resets the Snake at the Beginning Position Upon Dying
            self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]

            # Reset the Direction of the Snake
            self.direction = Vector2(1, 0)
        else:            
            self.body = [Vector2(5,15), Vector2(4,15), Vector2(3,15)]
            self.direction = Vector2(1, 0)

class FRUIT:
    def __init__(self):
        self.randomize()
        
    def draw_fruit(self):        
        # Create a rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)

        # Draw the rectangle
        #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        # Create an x and y position
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)      # Vectors are easier to work with than lists.

class MAIN:
    def __init__(self):
        # self.snake = SNAKE()
        self.snake_one = SNAKE(0)
        self.snake_two = SNAKE(1)
        # self.fruit = FRUIT()
        self.fruits = []
        self.create_fruits()

    def create_fruits(self):
        # Create 3 Fruits and STore in self.fruits list
        num_fruits = 3
        for i in range(num_fruits):
            self.fruits.append(FRUIT())

    def update(self):
        # self.snake.move_snake()
        self.snake_one.move_snake()
        self.snake_two.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        # Draw Objects
        self.draw_grass()
        # self.fruit.draw_fruit()        

        # Draw Every Fruit
        for fruit in self.fruits:
            fruit.draw_fruit()   

        # self.snake.draw_snake()  
        self.snake_one.draw_snake()
        self.snake_two.draw_snake()
        self.draw_score()  

    def check_collision(self):
        self.fruit_collision_verify(0)
        self.fruit_collision_verify(1)

        self.snake_collision_verify(0)
        self.snake_collision_verify(1)        

    def fruit_collision_verify(self, snake_flag: int):
        for fruit in self.fruits:
            if fruit.pos == self.snake_one.body[0]:
                # Play Crunch Sound
                self.snake_one.play_crunch_sound()

                # Grow the Snake - Add Another Block
                self.snake_one.add_block()                

            elif fruit.pos == self.snake_two.body[0]:                
                self.snake_two.play_crunch_sound()
                self.snake_two.add_block()

            # Make Sure That Fruit Does Not Spawn on Body of Snake
            while True:
                if fruit.pos in self.snake_one.body or fruit.pos in self.snake_two.body:
                    fruit.randomize()
                else:
                    break
        
    def snake_collision_verify(self, snake_flag: int):       
        if self.snake_one.body[0] == self.snake_two.body[0]:
            self.game_over(tie = True)      
        elif snake_flag == 0:
            if self.snake_one.body[0] in self.snake_two.body[1:]:
                self.game_over(winner = 1)
        elif snake_flag == 1:
            if self.snake_two.body[0] in self.snake_one.body[1:]:
                self.game_over(winner = 0)

    def check_fail(self):        
        self.snake_fail_verify(0)
        self.snake_fail_verify(1)

    def snake_fail_verify(self, snake_flag: int):
        if snake_flag == 0:   
            if self.snake_one.direction != Vector2(0, 0):     
                # Check If Snake One Is Not Out of Bounds on the X-axis
                if not 0 <= self.snake_one.body[0].x < cell_number:
                    self.game_over(1)

                # Check If Snake One Is Not Out of Bounds on the Y-axis
                if not 0 <= self.snake_one.body[0].y < cell_number:
                    self.game_over(1)

                # Check if Snake One Hits Itself
                for block in self.snake_one.body[1:]:
                    if block == self.snake_one.body[0]:
                        self.game_over(1)
    
        elif snake_flag == 1:  
            # Only check if snake_two has moved before applying failure conditions
            if self.snake_two.direction != Vector2(0, 0):
                # Check If Snake Two Is Not Out of Bounds on the X-axis
                if not 0 <= self.snake_two.body[0].x < cell_number:
                    self.game_over(0)

                # Check If Snake Two Is Not Out of Bounds on the Y-axis
                if not 0 <= self.snake_two.body[0].y < cell_number:
                    self.game_over(0)

                # Check if Snake Two Hits Itself
                for block in self.snake_two.body[1:]:
                    if block == self.snake_two.body[0]:
                        self.game_over(0)

    def game_over(self, winner = None, tie = False): 
        # self.snake.reset()
        if tie:
            self.print_winner(-1)            
        elif winner == 0:
            self.print_winner(0) 
        elif winner == 1:
            self.print_winner(1)

        # Update the display to ensure the winner text is shown
        pygame.display.update()

        # Wait for 3 seconds (3000 milliseconds) to allow the winner text to be visible
        pygame.time.wait(3000)

        # End the Game        
        pygame.quit()
        sys.exit()    

    def print_winner(self, winner_flag: int):
        if winner_flag == 0:
            # Find Score Location
            winner_text = "Player One Wins!"
        elif winner_flag == 1:
            winner_text = "Player Two Wins!"
        else:
            winner_text = "Tie Game! No Winner!"

        winner_surface = winner_font.render(winner_text,True,(56,74,12))  
        winner_x = int(cell_size * cell_number - 400)
        winner_y = int(cell_size * cell_number - 400)        
        winner_rect = winner_surface.get_rect(center = (winner_x, winner_y))       
        
        # Place a Background Around the Score
        bg_rect = pygame.Rect(winner_rect.left, winner_rect.top, winner_rect.width, winner_rect.height)
        pygame.draw.rect(screen, (167,209,61), bg_rect)

        # Draw a Frame Around the Score Box
        pygame.draw.rect(screen, (56,74,12), bg_rect, 2)

        # Draw the Score and Apple on the Screen 
        screen.blit(winner_surface, winner_rect)  
        
    def timer(self):
        timer_countdown = 5
        
        for i in range(timer_countdown, 0, -1):
            timer_text = f"{i}"            

            timer_surface = game_font.render(timer_text,True, (56,74,12))
            timer_x = int(cell_size * cell_number - 400)
            timer_y = int(cell_size * cell_number - 400)
            timer_rect = timer_surface.get_rect(center = (timer_x, timer_y))      

            # Draw a Frame Around the Score Box
            pygame.draw.rect(screen, (56,74,12), timer_rect, 2)

            # Draw the Score and Apple on the Screen 
            screen.blit(timer_surface, timer_rect)            

    def draw_grass(self):
        grass_color = (167,209,61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) 
                        pygame.draw.rect(screen, grass_color, grass_rect)   
            else:
                for col in range(cell_number):
                    if col % 2 == 1:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) 
                        pygame.draw.rect(screen, grass_color, grass_rect)   

    def draw_score(self):        
        self.draw_individual_score(0)
        self.draw_individual_score(1)

    def draw_individual_score(self, snake_flag: int):
        if snake_flag == 0:
            score_text = "P1 Score: " + str(len(self.snake_one.body) - 3)   # Reducing by 3 because we're starting with 3 blocks in our body
            
            score_surface = game_font.render(score_text,True, (56,74,12))
            score_x = int(cell_size * cell_number - 690)
            score_y = int(cell_size * cell_number - 60)
            score_rect = score_surface.get_rect(center = (score_x, score_y))
            
            # Find Apple Location
            apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

            # Place a Background Around the Score
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, (apple_rect.width + score_rect.width + 6), apple_rect.height)
            pygame.draw.rect(screen, (167,209,61), bg_rect)

            # Draw a Frame Around the Score Box
            pygame.draw.rect(screen, (56,74,12), bg_rect, 2)

            # Draw the Score and Apple on the Screen 
            screen.blit(score_surface, score_rect)
            screen.blit(apple,apple_rect)
        
        else:
            score_text = "P2 Score: " + str(len(self.snake_two.body) - 3)   # Reducing by 3 because we're starting with 3 blocks in our body
            #score_text = str(len(self.snake_two.body) - 3)

            score_surface = game_font.render(score_text,True, (56,74,12))
            score_x = int(cell_size * cell_number - 80)
            score_y = int(cell_size * cell_number - 60)
            score_rect = score_surface.get_rect(center = (score_x, score_y))
            
            # Find Apple Location
            apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

            # Place a Background Around the Score
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, (apple_rect.width + score_rect.width + 6), apple_rect.height)
            pygame.draw.rect(screen, (167,209,61), bg_rect)

            # Draw a Frame Around the Score Box
            pygame.draw.rect(screen, (56,74,12), bg_rect, 2)

            # Draw the Score and Apple on the Screen 
            screen.blit(score_surface, score_rect)
            screen.blit(apple,apple_rect)


# Used to Pre-Buffer the Sound Effects
pygame.mixer.pre_init(44100, -16, 2, 512)

# Starts the Entirety of the Game
pygame.init()       

# Main Game Window
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

# Clock Object to Set FPS
clock = pygame.time.Clock()

# Import a Fruit Image
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

# Create a Game Font
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

# Create a Winner Font
winner_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 75)

# Timers
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)   # Triggers every 150 ms

main_game = MAIN()

# Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            # Snake One Movement
            if event.key == pygame.K_UP:                
                if main_game.snake_one.direction.y != 1:
                    main_game.snake_one.direction = Vector2(0, -1)
                    direction_lock = True
            if event.key == pygame.K_DOWN:
                if main_game.snake_one.direction.y != -1:
                    main_game.snake_one.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake_one.direction.x != 1:
                    main_game.snake_one.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake_one.direction.x != -1:
                    main_game.snake_one.direction = Vector2(1, 0)
            
            # Snake Two Movement
            if event.key == pygame.K_w:                
                if main_game.snake_two.direction.y != 1:
                    main_game.snake_two.direction = Vector2(0, -1)
            elif event.key == pygame.K_s:
                if main_game.snake_two.direction.y != -1:
                    main_game.snake_two.direction = Vector2(0, 1)
            elif event.key == pygame.K_a:
                if main_game.snake_two.direction.x != 1:
                    main_game.snake_two.direction = Vector2(-1, 0)
            elif event.key == pygame.K_d:
                if main_game.snake_two.direction.x != -1:
                    main_game.snake_two.direction = Vector2(1, 0)            

    # Fill the Screen
    screen.fill((175, 215, 70))    

    # Draw elements
    main_game.draw_elements()    

    # Draw all of our elements    
    pygame.display.update() 

    # Set Framerate at 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()      # Ends any kind of code it's being run on