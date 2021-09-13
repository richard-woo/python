#一个电子相册
import os
import sys
import threading
import tkinter as tk
import time
from PIL import ImageTk, Image
import pygame
from mutagen.mp3 import MP3

class play_music:
    Path = r'music\\'