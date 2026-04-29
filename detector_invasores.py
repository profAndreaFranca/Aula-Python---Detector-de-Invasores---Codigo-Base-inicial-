import cv2
import time
import random

# ==============================
# CONFIGURAÇÕES INICIAIS
# ==============================

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
