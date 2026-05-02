# 🌆 Computer Graphics Sessional  
## **CSE-413 | MIST | Post-Earthquake City: Rescue and Recovery Visualization**

---

## 📌 Project Overview

This repository contains the complete coursework for the **Computer Graphics Sessional (CSE-413)** at the Military Institute of Science and Technology (MIST). It is organized into three parts:

1. **Lab Sessions** – Foundational OpenGL programming exercises in Python  
2. **Evaluation** – In-lab assessment tasks  
3. **Final 3D Project** – A full cinematic Blender animation titled *Post-Earthquake City: Rescue and Recovery Visualization*

The final project presents a **realistic 3D visualization of a city after a major earthquake**, focusing on the **human experience of disaster, rescue, and recovery**. The scene captures the aftermath of destruction while highlighting **modern emergency response systems**, including **rescue robots, drones, and coordinated human efforts**.

Using **computer graphics techniques such as realistic modeling, lighting, animation, and cinematic camera movement**, the project demonstrates how CG can effectively represent **real-world emergency situations** and communicate the importance of **technology-assisted rescue operations**.

---

## 📁 Repository Structure

```
Computer-Graphics-Sessional/
│
├── Day_01_Graphics_Sessional/       # Lab 1 — OpenGL Fundamentals
│   ├── Brief.txt                    # Lab brief & course overview
│   ├── DDA_Algorithm.py             # DDA line drawing algorithm
│   ├── Circle.py                    # Circle rendering with GLFW
│   ├── Rectangle.py                 # Rectangle rendering
│   ├── Triangle.py                  # Triangle rendering
│   ├── Hexagon.py                   # Hexagon rendering
│   └── House.py                     # House scene with shaders (VAO/VBO)
│
├── Day_02_Graphics_Sessional/       # Lab 2 — Animation & Interaction
│   ├── moving_triangle.py           # Continuously moving triangle
│   ├── triangle.py                  # Static triangle
│   └── bullet.py                    # 3D shooter game (player, enemies, bullets)
│
├── Evaluation/                      # In-lab Assessment Tasks
│   ├── Q1.py                        # Animated roadside scene (windmill + clouds)
│   ├── Q2.py                        # OpenGL square grid
│   ├── last_two_digits_id.py        # Draws last two digits of student ID
│   ├── last_two_letters_name.py     # Draws last two letters of student name
│   ├── House_rainbow_snowflake.py   # House with rainbow + snowflake effects
│   └── house_rainbow_rain.py        # House with rainbow + rain animation
│
└── README.md
```

---

## ⚙️ Environment Setup

> **Python 3.11 is required.** Other versions may cause compatibility issues with PyOpenGL.

### Verify your Python version
```bash
python --version
# or
python3 --version
```

### Install dependencies

```bash
# Core OpenGL bindings
pip install PyOpenGL PyOpenGL_accelerate

# Window & input backend — choose one:
pip install glfw        # Option A (recommended for most scripts)
pip install pygame      # Option B (used by House.py and shader examples)
```

### For the Final 3D Project (Blender)
- Download and install **Blender 2.8x or later** from [blender.org](https://blender.org)
- Blender runs standalone — no pip dependencies needed

---

## 🖥️ Lab Sessions

### Day 01 — OpenGL Fundamentals

| File | Description |
|---|---|
| `DDA_Algorithm.py` | Implements the **Digital Differential Analyzer** line drawing algorithm using `GL_POINTS`. Renders a white line from (50,50) to (400,300) on a 500×500 canvas using GLUT. |
| `Circle.py` | Draws a filled red circle using `GL_TRIANGLE_FAN` and `math.cos`/`math.sin`. Uses **GLFW** for window management. |
| `Rectangle.py` | Basic rectangle rendering with OpenGL primitives. |
| `Triangle.py` | Static triangle using basic OpenGL draw calls. |
| `Hexagon.py` | Regular hexagon drawn using polygon primitives. |
| `House.py` | A complete **modern OpenGL house scene** using custom GLSL vertex and fragment shaders, VAOs, and VBOs. Components: red roof (triangle), blue walls (quad), and a brown door. Uses **Pygame** as the display backend. |

**Key concepts covered:** `GL_POINTS`, `GL_TRIANGLES`, `GL_TRIANGLE_FAN`, `GL_QUADS`, orthographic projection (`gluOrtho2D`), GLSL shaders, VAO/VBO setup, GLFW and GLUT window management.

---

### Day 02 — Animation & Interaction

| File | Description |
|---|---|
| `moving_triangle.py` | A red triangle that **continuously moves left to right** across the screen and wraps around. Uses GLFW with a `time.sleep`-based loop. |
| `triangle.py` | Static triangle baseline used as a reference. |
| `bullet.py` | A fully functional **3D third-person shooter** built entirely in OpenGL/GLFW. Features a player with a gun, enemy cubes, bullet physics, a live score counter, lives system, invincibility frames after being hit, recoil, muzzle flash, and a camera that follows the player with yaw/pitch. |

**Key concepts covered:** Real-time animation loops, keyboard/mouse input, 3D transformations, `GL_QUADS` for cube faces, game state management, collision detection, delta-time physics.

---

## 📝 Evaluation Tasks

These were completed during in-lab assessments under time constraints.

| File | Task |
|---|---|
| `Q1.py` | Animated **2D roadside scene** with a continuously rotating windmill and moving clouds. Uses `gluOrtho2D(0,100,0,100)`, `GL_POLYGON`, `glutIdleFunc`, and double buffering (`GLUT_DOUBLE`). |
| `Q2.py` | Renders a **grid of squares** (50px cells) over a 500×500 window using `GL_LINES`. |
| `last_two_digits_id.py` | Draws the **last two digits of the student ID** ("54") manually using `GL_LINES` — each digit is individually constructed from line segments and transformed via `glTranslatef`. |
| `last_two_letters_name.py` | Draws the **last two letters of the student's name** manually using OpenGL line primitives. |
| `House_rainbow_snowflake.py` | A house scene extended with a **rainbow arc** and **animated snowflakes**. |
| `house_rainbow_rain.py` | Same house scene with a **rainbow** and **animated rain particles** falling over the scene. |

---

## 🎯 Final 3D Project — Objectives

- Visualize the **impact of a large-scale earthquake** on an urban environment  
- Showcase **modern rescue technologies** such as drones and autonomous robots  
- Highlight **human emotions and coordination** during disaster response  
- Demonstrate practical application of **computer graphics principles**  
- Create a **cinematic and storytelling-driven animation** suitable for academic evaluation  

---

## 🧩 Scene Breakdown

### **Scene 1 – Post-Earthquake City Overview**
- Aerial camera movement over collapsed buildings and damaged roads  
- Dust, debris, and smoke filling the environment  
- Emergency sirens and warning lights activated  
- Establishes the **scale and severity of destruction**

### **Scene 2 – Autonomous Drone Surveillance**
- Surveillance drones take off and scan the disaster zone  
- Spotlight or thermal-style scanning to locate survivors  
- Camera switches to **drone-level perspective**  
- Emphasizes **autonomous monitoring and reconnaissance systems**

### **Scene 3 – Ground-Level Rescue Robot Deployment**
- Rescue robots navigating through rubble-filled paths  
- Mechanical arm movements lifting debris  
- Wheel or track-based locomotion with realistic constraints  
- Close-up shots showcasing **rigged mechanical parts**

### **Scene 4 – Human Rescue Operations**
- Injured civilians signaling or attempting to move  
- Rescue workers coordinating with robots  
- Stretchers and emergency medical support introduced  
- Emotional storytelling achieved through **camera framing and composition**

### **Scene 5 – Emergency Vehicle Assistance**
- Ambulances and fire rescue trucks arriving on-site  
- Headlights, hazard lights, and rotating beacons activated  
- Coordinated movement between humans and machines  
- Reinforces the **organized emergency response system**

### **Scene 6 – Stabilization and Hope**
- Survivors being safely evacuated  
- Reduced dust and calmer lighting environment  
- Camera slowly pulls back to reveal a controlled rescue zone  
- Symbolizes **recovery, hope, and technological support**

---

## 🏗️ 3D Assets & Objects

### Environment & Infrastructure
- Cracked road, sidewalk, broken walls  
- Collapsed buildings, fallen electric poles  
- Debris, rubble, cables and exposed pipes  
- Damaged lab classroom interior  

### Rescue & Emergency Equipment
- Fire rescue truck, ambulance  
- Emergency warning cones, flashlights  
- Medical kits, stretchers, emergency lights  

### Technology & Machines
- Surveillance drone  
- Rescue robot with robotic arm unit  

### Characters
- Rescue workers, medical personnel  
- Walking survivors, injured civilians  

### Visual Effects
- Smoke effects, dust particles  
- Warning and hazard lights  

---

## 🛠️ Technical Focus Areas

| Area | Details |
|---|---|
| **3D Modeling** | Buildings, vehicles, robots, characters, environment |
| **Texturing & Materials** | Damaged surfaces, metallic parts, debris textures |
| **Lighting** | Emergency lighting, smoke interaction, mood-based lighting, emission animation |
| **Rigging** | Character armatures, robotic arm joints |
| **Animation** | Camera movement (aerial, ground, cinematic), mechanical animation (robots, drones), character motion |
| **Visual Effects** | Smoke, dust, particle systems, CONSTANT interpolation for flashing lights |
| **Rendering** | Cycles render engine, multi-shot camera system with scene markers |

---

## 🎥 Visual Style

- Semi-realistic to realistic visual approach  
- Cinematic camera transitions and pacing  
- Emotional framing to emphasize human struggle and hope  
- Balanced focus on **technology and humanity**

---

## 📊 Grading Breakdown

| Component | Weightage |
|---|---|
| 3D Project (total) | 50–60% |
| — Proposal | 5–10% |
| — Project Update 1 | 10% |
| — Project Update 2 | 10% |
| 2D Evaluation + Assessment | 35% |
| 3D Report + Final Presentation | 10% |
| Observation (Participation & Progress) | 5% |

---

## ✅ Project Significance

This project demonstrates how **computer graphics can be used beyond entertainment**, serving as a powerful tool for:
- Disaster awareness  
- Emergency response visualization  
- Educational and simulation purposes  

It reflects a **moderate-level academic CG project** that combines **technical skill, storytelling, and real-world relevance**.

---

## ✨ Conclusion

The **Post-Earthquake City: Rescue and Recovery Visualization** project showcases the effective use of computer graphics to simulate emergency scenarios, highlight technological advancements, and convey human resilience—making it both **technically sound and narratively impactful**. The accompanying OpenGL lab exercises build up the foundational 2D/3D rendering knowledge that feeds into the larger Blender project.
