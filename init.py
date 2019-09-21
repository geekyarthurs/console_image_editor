from models.Utils.ColorPrint import ColorPrint
import cv2
import json
import sys
import os

with open('config/messages.json', 'r') as f:
    messages = json.load(f)
    error_messages = messages["errors"]