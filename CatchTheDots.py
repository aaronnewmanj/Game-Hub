import pygame
import random
import time
import math

def open_game3():
    pygame.init()

    screen_width = 1400
    screen_height = 850
    fill_color = (0,0,0)

    circle_colors = [(255, 0, 0), (0, 255, 0)]
    circle_rad = 35
    circle_num = 25


    start_time = time.time()
    time_limit = 20

    font = pygame.font.Font(None, 130)



    class Circle:
        def __init__(self, x, y, radius, color=(0,0,0)):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        def get_x(self):
            return self.x
        def get_y(self):
            return self.y
        def get_color(self):
            return self.color


    circles = []


    screen = pygame.display.set_mode((screen_width, screen_height))

    running = True
    g_count = 0

    for i in range(circle_num):
        x = random.randint(0+circle_rad, screen_width-circle_rad)
        y = random.randint(0+circle_rad, screen_height-circle_rad)
        color = random.choice(circle_colors)
        if color==circle_colors[1]:
            g_count+=1
        circles.append(Circle(x, y, circle_rad, color))

    caught = 0


    while running: #this loops every single frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        current_time = time.time()
        elapsed_time = current_time - start_time
        time_left = math.floor(time_limit-elapsed_time+1)

        screen.fill(fill_color)

        text_surface = font.render(str(time_left), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, screen_height // 2)
        
        screen.blit(text_surface, text_rect)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for c in circles:
            c.draw(screen)
            if mouse_x>=c.get_x()-circle_rad and mouse_x<=c.get_x()+circle_rad:
                if mouse_y>=c.get_y()-circle_rad and mouse_y<=c.get_y()+circle_rad:
                    if c.get_color()==circle_colors[0]:
                        running = False
                        print("You lost! You hit a red dot.")
                        print("You caught", caught, "green dots.")
                        print("")
                    elif c.get_color()==circle_colors[1]:
                        caught+=1

                    circles.remove(c)

                    if caught==g_count:
                        running=False
                        print("You won with", time_left, "seconds left!")
                        print("You caught", caught, "green dots.")
                        print("")

        if elapsed_time >= time_limit:
            running = False
            print("Time's up! You Lost!")
            print("You caught", caught, "green dots.")
            print("")
            
        pygame.display.flip()

    pygame.quit()

        

        

        



