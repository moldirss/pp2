import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    trail_enabled = True  # Enables trail following the mouse
    eraser_mode = False

    def drawLineBetween(screen, index, start, end, width, color_mode):
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))

        if color_mode == 'blue':
            color = (c1, c1, c2)
        elif color_mode == 'red':
            color = (c2, c1, c1)
        elif color_mode == 'green':
            color = (c1, c2, c1)
        elif color_mode == 'eraser':
            color = (0, 0, 0)  # Black for erasing

        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))

        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            pygame.draw.circle(screen, color, (x, y), width)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held or (event.key == pygame.K_F4 and alt_held):
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Color selection keys
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode  # Toggle eraser mode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click increases radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # Right click decreases radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and trail_enabled:
                position = event.pos
                points = points + [position]
                points = points[-256:]  # Keep the last 256 points for performance

        # Clear screen on each frame
        screen.fill((0, 0, 0))

        # Draw trail
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, 'eraser' if eraser_mode else mode)
            i += 1

        pygame.display.flip()
        clock.tick(60)

main()
