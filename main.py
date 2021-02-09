import cv2
import numpy as np
from tqdm import tqdm
from time import sleep

video_source = ('source.mp4')
capture = cv2.VideoCapture(video_source)
threshold = 0.5
font = cv2.FONT_HERSHEY_DUPLEX
altura_min, largura_min = 80, 80

conectado, video = capture.read()

bounding_box = cv2.selectROI("Regiao de Interesse", video, False)
cv2.destroyAllWindows()

#try:
car_size = cv2.selectROI("Tamanho minimo do Objeto, Esc para usar default (Carro pequeno)", video, False)
a1, b1, larg, alt = (car_size[i] for i in range(4))
altura_min, largura_min = alt, larg
if car_size == (0, 0, 0, 0):
    altura_min, largura_min = 80, 80
    
cv2.destroyAllWindows()


x1, y1, w, h = (bounding_box[i] for i in range(4))

x2 = x1 + w
y2 = y1 + h

# Saída

frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
fps = capture.get(cv2.CAP_PROP_FPS)

nome_arquivo = 'resultado.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_altura = video.shape[0]
video_largura = video.shape[1]
saida_video = cv2.VideoWriter(nome_arquivo, fourcc, fps, (video_largura, video_altura))
c = 0
carro = False

subtraction = cv2.bgsegm.createBackgroundSubtractorMOG()

for c in tqdm(range(frame_count)):
    
    conectado, frame = capture.read()

    if not conectado:
        break
    
    if conectado:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        interest = frame[y1:y2, x1:x2]
        
        delay = float(1 / fps)
        sleep(delay)
        
        img = cv2.cvtColor(interest, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 5)
        img = subtraction.apply(img)
        img = cv2.dilate(img, np.ones((5, 5)))
        
        morf = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, morf)
        result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, morf)
        
        contorno, imagem = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        carro = False
        
        for i, j in enumerate(contorno):
            (x, y, w, h) = cv2.boundingRect(j)
            if w >= largura_min and h >= altura_min:
                carro = True
                cv2.rectangle(frame, (x1 + x, y1 + y), (x1 + x + w, y1 + y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Carro", (x1 + x, y1 + y - 5), font, 0.6, (0, 255, 0), 2)
        
        saida_video.write(frame)

        c += 1
        
    if cv2.waitKey(1) == 27:
        break
            
capture.release()
saida_video.release()
cv2.destroyAllWindows()
    