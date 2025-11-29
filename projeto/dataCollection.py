import cv2
import math
from cvzone.HandTrackingModule import HandDetector
import numpy as np



cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

dist = 20
TAMANHOIMG = 300


window_name = "Image"
while True:
    
    #success -> boolean
    #img -> imagem da câmera
    (success, img) = cap.read()
    #outra tupla
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        #hand2 = hand[1]
        posiX, posiY, largura, altura = hand['bbox']




        #Criando uma matriz numpy -> com valor (1,1,1) para cada pixel
        #np.ones(<tamanho em pixels, largura em pixels, canal de cor>, <tipo de dados dois pixels>)
        #imageVermelha -> ([1,1,1], canalTyp)
        imageVermelha = np.ones((TAMANHOIMG, TAMANHOIMG, 3), np.uint8)
        #faz com que o canal R seja 255
        imageVermelha[:,:, 2] *= 255




        #print(f"({posiX},{posiY})")
        #print(f"altura: {altura}, largura: {largura}")
        

        #Codigo para verificar se não está ocorrendo estouro de borda
        if(posiY - dist> 0 and posiX - dist > 0):
            recorteImagem = img[posiY - dist: posiY + altura + dist, posiX - dist: posiX + largura + dist]

            #shape -> retorna uma matriz de três valores [altura, largura, canal]
            recorteImagemTamanho = recorteImagem.shape

            #Verifica de o tamanho da imagem da mão não ultrapassa a grade de imagemVermelha
            if(recorteImagemTamanho[0] < TAMANHOIMG and recorteImagemTamanho[1] < TAMANHOIMG):

                comparaDimen = altura/largura

                if (comparaDimen > 1):
                    k = TAMANHOIMG/altura
                    larguraCall = math.ceil(k*largura)

                    imgResize = cv2.resize(recorteImagem, (larguraCall, TAMANHOIMG))
                    imgResizeTamanho = imgResize.shape

                    #Clipando a imagem recorte na imagemVermelha -> imagemVermelha[largura, altura] = recorteImagem
                    imageVermelha[0:imgResizeTamanho[0], 0:imgResizeTamanho[1]] = recorteImagem

            cv2.imshow("recorteImagem", recorteImagem)
            cv2.imshow("imagemBranca", imageVermelha)


    #mostra a img em uma janela GUI (Graphcs User Interface)
    cv2.imshow("Image", img)
    #delay de 1 ms
    cv2.waitKey(1)
    

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break
    