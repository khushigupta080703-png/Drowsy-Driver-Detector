# Day 1 - Setup verification script
# This script checks all libraries are installed correctly

import sys

print("=" * 50)
print("Drowsy Driver Detector - Day 1 Setup Test")
print("=" * 50)

# Test 1: Python version
print(f"\n Python version: {sys.version}")

# Test 2: OpenCV
try:
    import cv2
    print(f" OpenCV version: {cv2.__version__}")
except ImportError:
    print(" OpenCV NOT installed")

# Test 3: dlib
try:
    import dlib
    print(f" dlib version: {dlib.__version__}")
except ImportError:
    print(" dlib NOT installed")

# Test 4: numpy
try:
    import numpy as np
    print(f" NumPy version: {np.__version__}")
except ImportError:
    print(" NumPy NOT installed")

# Test 5: pandas
try:
    import pandas as pd
    print(f" Pandas version: {pd.__version__}")
except ImportError:
    print(" Pandas NOT installed")

# Test 6: Flask
try:
    import flask
    print(f" Flask version: {flask.__version__}")
except ImportError:
    print(" Flask NOT installed")

# Test 7: pygame
try:
    import pygame
    print(f" Pygame version: {pygame.__version__}")
except ImportError:
    print(" Pygame NOT installed")

print("\n" + "=" * 50)
print(" All libraries checked!")
print(" Day 1 Complete - Ready for Day 2")
print("=" * 50)



