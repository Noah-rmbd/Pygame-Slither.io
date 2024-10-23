import random

import pygame
import math
import sys

# Initialiser Pygame
pygame.init()

def calculate_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 1800, 1600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boule qui suit le curseur")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Propriétés de la boule
ball_radius = 10
ball_speed = 5
turn_speed = 20   #bornée par [20, 10] 20 étant au début le meilleur et 10 le pire
angle = 0

ball_x = 400
ball_y = 300
segments = [[ball_x, ball_y],[ball_x-1, ball_y-1],[ball_x-2, ball_y-2],[ball_x-3, ball_y-3]]

color = (0,0,255)

increase_length = False

nb_objets = 30

for objet in range(nb_objets):
    print("Hey")
    x_obj = random.randint(0,800)
    y_obj = random.randint(0,600)
    #objet =
    pygame.draw.circle(screen, (random.randint(0,255),random.randint(0,255), random.randint(0,255)), (x_obj, y_obj),
                       3)

# Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Détecter si une touche est pressée ou relâchée
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_speed = 10  # Augmenter la vitesse quand la barre d'espace est enfoncée
            elif event.key == pygame.K_m:
                increase_length = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                ball_speed = 5  # Revenir à la vitesse normale lorsque la barre d'espace est relâchée

    # Remplir l'écran avec une couleur de fond
    screen.fill(WHITE)

    # Obtenir la position du curseur
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculer l'angle entre la boule et le curseur
    target_angle = calculate_angle(ball_x, ball_y, mouse_x, mouse_y)

    # Calculer la différence entre l'angle actuel et l'angle cible
    angle_diff = (target_angle - angle) % (2 * math.pi)

    # Ajuster l'angle progressivement (braquage limité)
    if angle_diff > math.pi:  # Si l'angle_diff dépasse π, tourner dans l'autre sens
        angle_diff -= 2 * math.pi
    if abs(angle_diff) > turn_speed * math.pi / 180:  # Limiter l'ajustement de l'angle à chaque frame
        angle += turn_speed * math.pi / 180 * math.copysign(1, angle_diff)  # Ajuster l'angle par incréments
    else:
        angle = target_angle  # Si la différence est petite, on aligne directement l'angle

    # Calculer les nouvelles coordonnées de la boule
    ball_x += math.cos(angle) * ball_speed
    ball_y += math.sin(angle) * ball_speed


    for ball in range(len(segments)-1, 0, -1):
        segments[ball] = segments[ball-1].copy()

    if increase_length:
        segments.append(segments[-1].copy())
        increase_length = False

    segments[0] = [ball_x, ball_y]

    # Dessiner la boule à la position du curseur
    nb = 1
    for ball in segments:
        ball_radius = 10 + 10 * (len(segments)^2)/100
        pygame.draw.circle(screen, (color[0]+nb*2, color[1]+nb*2, color[2]-nb*2), (ball[0], ball[1]), ball_radius)
        nb += 1

    turn_speed = 20 - 10 * (len(segments))/100
    if len(segments) > 100:
        turn_speed = 10
    print(len(segments), turn_speed)
    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()
