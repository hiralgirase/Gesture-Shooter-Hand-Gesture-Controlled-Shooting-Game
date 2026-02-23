# Gesture Shooter -- Hand Gesture Controlled Shooting Game

## Overview

Gesture Shooter is a real-time gesture-controlled shooting game built
using Computer Vision, MediaPipe hand tracking, OpenCV, and Pygame. The
system replaces traditional keyboard controls with live hand gestures
captured via a webcam.

The game detects hand landmarks in real time, interprets predefined
gestures, and maps them to in-game actions such as player movement and
shooting.

------------------------------------------------------------------------

## Features

-   Real-time webcam-based hand tracking
-   MediaPipe hand landmark detection
-   Gesture-based shooting mechanism
-   Modular game architecture
-   Collision detection system
-   Explosion animations and enemy logic
-   Organized asset management
-   Structured project documentation

------------------------------------------------------------------------

## System Architecture

Webcam\
↓\
OpenCV Frame Capture\
↓\
MediaPipe Hand Landmark Detection\
↓\
Gesture Detection Module\
↓\
Game Logic (Player / Enemy / Bullets)\
↓\
Rendering & Collision Handling

------------------------------------------------------------------------

## Project Structure

GESTURE_SHOOTER/

├── **pycache**/\
├── assets/ \# Game images, sounds, sprites\
├── clean_env/ \# Virtual environment (optional)\
├── models/ \# Gesture/hand tracking models\
│\
├── bullet.py \# Player bullet logic\
├── enemy_bullet.py \# Enemy bullet logic\
├── enemy.py \# Enemy behavior & movement\
├── explosion.py \# Explosion animation\
├── gesture_detector.py \# Hand detection & gesture logic\
├── player.py \# Player movement & rendering\
├── main.py \# Main game execution\
│\
├── hand_landmarker.task \# MediaPipe hand model file\
├── game-documents.pdf \# Project documentation\
├── gesture-control-game-documents.pdf\
├── How To Run The Code.txt

------------------------------------------------------------------------

## Technologies Used

-   Python\
-   OpenCV\
-   MediaPipe\
-   Pygame\
-   NumPy

------------------------------------------------------------------------

## Installation

1.  Clone the repository:

git clone https://github.com/hiralgirase/gesture-shooter.git\
cd gesture-shooter

2.  Install required libraries:

pip install opencv-python mediapipe pygame numpy

------------------------------------------------------------------------

## How to Run

Ensure the file `hand_landmarker.task` is present in the project
directory.

Run the main file:

python main.py

Make sure your webcam is connected and accessible.

------------------------------------------------------------------------

## Gameplay Description

-   Player movement is controlled using hand gestures.
-   Shooting is triggered through predefined finger configurations.
-   Enemies spawn dynamically.
-   Collision detection manages damage and explosion effects.
-   Player health and score are tracked during gameplay.

------------------------------------------------------------------------

## Module Description

gesture_detector.py\
Handles hand landmark detection and gesture classification.

player.py\
Manages player movement, rendering, and health.

enemy.py\
Controls enemy spawning, movement, and attack logic.

bullet.py / enemy_bullet.py\
Handles projectile movement and collision detection.

explosion.py\
Manages explosion animation effects.

main.py\
Coordinates overall game flow, rendering, and event handling.

------------------------------------------------------------------------

## Future Improvements

-   Multi-hand gesture support
-   Gesture customization settings
-   Dynamic difficulty scaling
-   Advanced enemy AI behavior
-   Performance optimization
-   Cross-platform support

------------------------------------------------------------------------

## Limitations

-   Performance depends on lighting conditions
-   Background clutter may affect detection accuracy
-   Requires stable webcam positioning
-   Real-time processing may increase CPU usage

------------------------------------------------------------------------

## License

MIT License

------------------------------------------------------------------------

## Author

Hiral Girase\
Computer Vision & Interactive AI Systems
