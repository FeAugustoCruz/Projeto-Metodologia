import cv2
import math
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

window_name = "Image"
while True:
    
    #success -> boolean
    #img -> imagem da câmera
    (success, img) = cap.read()
    #outra tupla
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        posiX, posiY, largura, altura = hand['bbox']
        #print(f"({posiX},{posiY})")
        print(f"y: {posiY + altura}, x: {posiX + largura}")
        #print(f"w: {w}")
        #print(f"h: {h}")
        if(posiY > 0 and posiX > 0):
            recorteImagem = img[posiY: posiY + altura, posiX: posiX + largura]
            cv2.imshow("recorteImagem", recorteImagem)
    #mostra a img em uma janela GUI
    cv2.imshow("Image", img)
    #delay de 1 ms
    cv2.waitKey(1)
    

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break
    