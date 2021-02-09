import cv2
import numpy as np
from tqdm import tqdm

# Configurações Iniciais
video_source = ('source.mp4')
threshold = 0.5
altura_min, largura_min = 80, 80
font = cv2.FONT_HERSHEY_DUPLEX

# Abrindo o vídeo para obter informações
capture = cv2.VideoCapture(video_source)
conectado, video = capture.read()
frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
fps = capture.get(cv2.CAP_PROP_FPS)

# Definindo Região de Interesse
bounding_box = cv2.selectROI("Regiao de Interesse", video, False)
cv2.destroyAllWindows()
x1, y1, w, h = (bounding_box[i] for i in range(4))
x2 = x1 + w
y2 = y1 + h

# Definindo Tamanho do Alvo de Captura
car_size = cv2.selectROI("Tamanho minimo do Objeto, Esc para usar default (Carro pequeno)", video, False)
a1, b1, larg, alt = (car_size[i] for i in range(4))
altura_min, largura_min = alt, larg
if car_size == (0, 0, 0, 0):
    altura_min, largura_min = 80, 80
cv2.destroyAllWindows()

# Saída
nome_arquivo = 'resultado.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_altura = video.shape[0]
video_largura = video.shape[1]
saida_video = cv2.VideoWriter(nome_arquivo, fourcc, fps, (video_largura, video_altura))

# Inicializando variáveis
c = 0
alvo = False
subtraction = cv2.bgsegm.createBackgroundSubtractorMOG()

# Loop Principal
for c in tqdm(range(frame_count)):
    #Checa se arquivo já terminou de rodar e capta frame como imagem
    conectado, frame = capture.read()

    if not conectado:
        break

    else:
        #Definindo e desenhando área de interesse
        interest = frame[y1:y2, x1:x2]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        #Processamento da imagem
        img = cv2.cvtColor(interest, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (3, 3), 5)
        img = subtraction.apply(img)
        img = cv2.dilate(img, np.ones((5, 5)))
        
        morf = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        
        result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, morf)
        result = cv2.morphologyEx(result, cv2.MORPH_CLOSE, morf)
        
        #Função do OpenCV para encontrar objetos em movimento
        contorno, imagem = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        alvo = False
        
        #Para cada objeto em movimento, verificar se é maior que o mínimo pedido
        for i, j in enumerate(contorno):
            (x, y, w, h) = cv2.boundingRect(j)
            if w >= largura_min and h >= altura_min:
                alvo = True
                #Desenhando retangulos em torno dos alvos encontrados
                cv2.rectangle(frame, (x1 + x, y1 + y), (x1 + x + w, y1 + y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Alvo", (x1 + x, y1 + y - 5), font, 0.6, (0, 255, 0), 2)
        
        #Escreve o frame na saída
        saida_video.write(frame)

        #Contador para a barra de progresso
        c += 1
        
    if cv2.waitKey(1) == 27:
        break

#Liberando arquivos e finalizando
capture.release()
saida_video.release()
cv2.destroyAllWindows()
