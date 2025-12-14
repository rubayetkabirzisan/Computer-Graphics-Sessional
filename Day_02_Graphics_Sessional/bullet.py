import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# --- Constants ---
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768

# Balance
PLAYER_SPEED = 8.0
ROTATION_SPEED = 120.0
BULLET_SPEED = 50.0
FIRE_RATE = 0.2 
RECOIL_FORCE = 0.2
RECOIL_RECOVERY = 2.0
INVULNERABILITY_TIME = 2.0  # Seconds of safety after getting hit

# --- Global State ---
player_pos = [0.0, 1.0, 0.0]
player_lives = 5
score = 0
game_over = False

cam_yaw = -90.0
cam_pitch = 0.0
cam_dist = 8.0

# Timers
recoil_offset = 0.0
last_shot_time = 0.0
muzzle_flash_timer = 0.0
invuln_timer = 0.0  # Timer for invincibility

bullets = [] 
enemies = []

# --- 3D Models ---

def draw_cube(size, r, g, b):
    s = size / 2.0
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    for x, y, z in [
        (-s,-s, s), ( s,-s, s), ( s, s, s), (-s, s, s), # Front
        (-s,-s,-s), (-s, s,-s), ( s, s,-s), ( s,-s,-s), # Back
        (-s,-s,-s), (-s,-s, s), (-s, s, s), (-s, s,-s), # Left
        ( s,-s,-s), ( s, s,-s), ( s, s, s), ( s,-s, s), # Right
        (-s, s,-s), (-s, s, s), ( s, s, s), ( s, s,-s), # Top
        (-s,-s,-s), ( s,-s,-s), ( s,-s, s), (-s,-s, s)  # Bottom
    ]:
        glVertex3f(x, y, z)
    glEnd()

def draw_player_with_gun():
    # Flashing effect if invincible
    if invuln_timer > 0:
        # Blink every 0.1 seconds
        if int(invuln_timer * 10) % 2 == 0:
            return # Don't draw this frame (invisible)

    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glRotatef(cam_yaw + 90, 0, 1, 0) 

    # Body
    draw_cube(1.0, 0.0, 0.8, 0.0)
    # Visor
    glPushMatrix()
    glTranslatef(0.3, 0.2, 0.51); glScalef(0.8, 0.2, 0.1)
    draw_cube(1.0, 0.0, 0.0, 0.0)
    glPopMatrix()
    # Gun
    glPushMatrix()
    glTranslatef(0.6, 0.0, 0.4 - recoil_offset) 
    glScalef(0.2, 0.2, 1.2)
    draw_cube(1.0, 0.3, 0.3, 0.3)
    glPopMatrix()
    # Flash
    if muzzle_flash_timer > 0:
        glPushMatrix()
        glTranslatef(0.6, 0.0, 1.1 - recoil_offset)
        s = random.uniform(0.3, 0.6); glScalef(s, s, s)
        draw_cube(1.0, 1.0, 1.0, 0.0)
        glPopMatrix()
    glPopMatrix()

def draw_scene_objects():
    glBegin(GL_LINES)
    glColor3f(0.2, 0.2, 0.2)
    for i in range(-40, 41, 4):
        glVertex3f(i, 0, -40); glVertex3f(i, 0, 40)
        glVertex3f(-40, 0, i); glVertex3f(40, 0, i)
    glEnd()
    for e in enemies:
        glPushMatrix()
        glTranslatef(e[0], e[1], e[2])
        draw_cube(1.2, 1.0, 0.1, 0.1)
        glPopMatrix()
    for b in bullets:
        glPushMatrix()
        glTranslatef(b['pos'][0], b['pos'][1], b['pos'][2])
        glScalef(0.1, 0.1, 0.6)
        draw_cube(1.0, 1.0, 1.0, 0.0)
        glPopMatrix()

def draw_hud():
    glMatrixMode(GL_PROJECTION); glPushMatrix(); glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW); glLoadIdentity(); glDisable(GL_DEPTH_TEST)
    
    # 1. Crosshair
    cx, cy = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
    glColor3f(0, 1, 0); glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(cx-20, cy); glVertex2f(cx+20, cy)
    glVertex2f(cx, cy-20); glVertex2f(cx, cy+20)
    glEnd()

    # 2. Lives Display (Top Left)
    start_x = 20
    start_y = 20
    box_size = 20
    gap = 5
    
    # Draw a box for each life
    for i in range(player_lives):
        glColor3f(0.0, 1.0, 0.0) # Green Life
        x = start_x + (box_size + gap) * i
        glBegin(GL_QUADS)
        glVertex2f(x, start_y)
        glVertex2f(x + box_size, start_y)
        glVertex2f(x + box_size, start_y + box_size)
        glVertex2f(x, start_y + box_size)
        glEnd()

    glEnable(GL_DEPTH_TEST); glMatrixMode(GL_PROJECTION); glPopMatrix(); glMatrixMode(GL_MODELVIEW)

# --- Logic ---

def get_gun_muzzle_pos():
    rad = math.radians(cam_yaw)
    wx = player_pos[0] + (0.6 * math.cos(rad) + 1.0 * math.sin(rad))
    wz = player_pos[2] + (-0.6 * math.sin(rad) + 1.0 * math.cos(rad))
    return [wx, player_pos[1], wz]

def shoot():
    global bullets, last_shot_time, recoil_offset, muzzle_flash_timer
    
    recoil_offset = RECOIL_FORCE
    muzzle_flash_timer = 0.05
    
    rad_yaw = math.radians(cam_yaw)
    rad_pitch = math.radians(cam_pitch)
    
    dx = math.sin(rad_yaw) * math.cos(rad_pitch)
    dy = math.sin(rad_pitch)
    dz = -math.cos(rad_yaw) * math.cos(rad_pitch)

    bullets.append({'pos': get_gun_muzzle_pos(), 'dir': [dx, dy, dz], 'life': 2.0})

def key_callback(w, k, s, a, m):
    global game_over, score, player_lives, enemies, bullets
    if a == glfw.PRESS:
        if k == glfw.KEY_ESCAPE: glfw.set_window_should_close(w, True)
        if k == glfw.KEY_R and game_over:
            # Restart
            game_over = False; score=0; player_lives=5; enemies=[]; bullets=[]

def main():
    global player_pos, recoil_offset, muzzle_flash_timer, game_over, score, player_lives, cam_yaw, cam_pitch, last_shot_time, invuln_timer

    glfw.init()
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Spacebar Shooter", None, None)
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_NORMAL)
    
    glEnable(GL_DEPTH_TEST)
    last_time = glfw.get_time()
    last_spawn = 0

    while not glfw.window_should_close(window):
        t = glfw.get_time()
        dt = t - last_time
        last_time = t

        if not game_over:
            # --- INPUT ---
            # 1. Rotation (Arrow Keys)
            rot_amount = ROTATION_SPEED * dt
            if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS: cam_yaw -= rot_amount
            if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS: cam_yaw += rot_amount
            if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS: cam_pitch += rot_amount
            if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS: cam_pitch -= rot_amount
            cam_pitch = max(-80, min(80, cam_pitch))

            # 2. Movement (WASD)
            rad = math.radians(cam_yaw)
            s = math.sin(rad); c = math.cos(rad)
            dx, dz = 0, 0
            if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS: dz -= c; dx += s
            if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS: dz += c; dx -= s
            if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS: dz -= s; dx -= c
            if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS: dz += s; dx += c
            
            length = math.hypot(dx, dz)
            if length > 0:
                player_pos[0] += (dx/length) * PLAYER_SPEED * dt
                player_pos[2] += (dz/length) * PLAYER_SPEED * dt

            # 3. Shooting (SPACEBAR)
            if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
                if t - last_shot_time >= FIRE_RATE:
                    shoot()
                    last_shot_time = t

            # --- LOGIC ---
            if recoil_offset > 0: recoil_offset -= RECOIL_RECOVERY * dt
            if muzzle_flash_timer > 0: muzzle_flash_timer -= dt
            if invuln_timer > 0: invuln_timer -= dt

            # Update Bullets
            for b in bullets[:]:
                b['pos'][0] += b['dir'][0] * BULLET_SPEED * dt
                b['pos'][1] += b['dir'][1] * BULLET_SPEED * dt
                b['pos'][2] += b['dir'][2] * BULLET_SPEED * dt
                b['life'] -= dt
                if b['life'] <= 0 or b['pos'][1] < 0: bullets.remove(b)

            # Spawn Enemies
            if t - last_spawn > 1.2:
                last_spawn = t
                ang = random.uniform(0, 6.28); dist = random.uniform(20, 35)
                enemies.append([player_pos[0]+math.sin(ang)*dist, 1.0, player_pos[2]+math.cos(ang)*dist])

            # Enemy Collisions
            for e in enemies[:]:
                vx, vz = player_pos[0]-e[0], player_pos[2]-e[2]
                dist = math.hypot(vx, vz)
                if dist > 0: e[0]+=vx/dist*4.0*dt; e[2]+=vz/dist*4.0*dt
                
                # Player HIT Logic
                if dist < 1.5:
                    if invuln_timer <= 0: # Only take damage if not invincible
                        player_lives -= 1
                        invuln_timer = INVULNERABILITY_TIME # Become invincible
                        print(f"Hit! Lives remaining: {player_lives}")
                        
                        if player_lives <= 0: 
                            game_over = True
                
                # Bullet HIT Logic
                for b in bullets[:]:
                    if math.hypot(e[0]-b['pos'][0], e[2]-b['pos'][2]) < 1.5:
                        if e in enemies: enemies.remove(e)
                        if b in bullets: bullets.remove(b)
                        score += 50; break

        # --- RENDER ---
        glClearColor(0.1, 0.15, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION); glLoadIdentity()
        gluPerspective(60, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100)
        glMatrixMode(GL_MODELVIEW); glLoadIdentity()
        
        rad_y = math.radians(cam_yaw)
        rad_p = math.radians(cam_pitch)
        eye_x = player_pos[0] - cam_dist * math.sin(rad_y) * math.cos(rad_p)
        eye_y = player_pos[1] + cam_dist * math.sin(rad_p) + 2.0
        eye_z = player_pos[2] + cam_dist * math.cos(rad_y) * math.cos(rad_p)
        gluLookAt(eye_x, eye_y, eye_z, player_pos[0], player_pos[1]+1.0, player_pos[2], 0, 1, 0)

        draw_scene_objects()
        if not game_over: draw_player_with_gun()
        draw_hud()
        
        glfw.set_window_title(window, f"Lives: {player_lives} | Score: {score}" if not game_over else "GAME OVER (Press R)")
        glfw.swap_buffers(window); glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()