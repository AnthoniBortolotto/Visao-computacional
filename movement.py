import cv2
import numpy as np
valor = 'images/shot00'

# valor nulo para comparar para saber se é a primeira imagem
antigo = None

for i in range(3, 16):
    normNumber = i
    if i < 10:
        normNumber = '0' + str(i)
    path = valor + str(normNumber) + '.png'
    # Carregar a imagem
    fator = 0.5
    imagem = cv2.imread(path)
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    if (antigo is not None):
        diferenca = cv2.absdiff(gray, antigo)
        
        # corrige mudanças de iluminação nas imagens
        ilumination_change = cv2.threshold(diferenca, 25, 255, cv2.THRESH_BINARY)[1]
        num = cv2.countNonZero(ilumination_change) / (gray.size / 100)
        if(num > 10):
            media = cv2.mean(diferenca)[0]


            matriz_resultante = np.maximum(gray * 1.8, 0).astype(np.uint8)
            #matriz_resultante = np.minimum(gray / 0.53, 255).astype(np.uint8)
            diferenca = cv2.absdiff(matriz_resultante , antigo)

            cv2.imshow('Imagem', diferenca)
        
        
        #print(diferenca)
        #cv2.imshow('Imagem', diferenca)
        cv2.waitKey(0)
    antigo = gray
# Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro ao carregar a imagem")
    else:
    # Exibir a imagem em uma janela
        #print(imagem)
        cv2.waitKey(0)  # Esperar até uma tecla ser pressionada
        cv2.destroyAllWindows()  # Fechar todas as janelas abertas


