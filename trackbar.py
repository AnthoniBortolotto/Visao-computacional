import cv2

#change the path to the folder where the images are
base_path = 'C:/Users/Dell/Documents/repos/visao/Visao-computacional/'
valor = base_path + 'images/shot00'

# valor nulo para comparar para saber se é a primeira imagem
antigo = None


def on_trackbar_change (i):
    global antigo
    # Obtenha o valor atual da trackbar 'i'
    print(i)
    normNumber = i + 3
    if normNumber < 10:
        normNumber = '0' + str(normNumber)
    path = valor + str(normNumber) + '.png'
    
    # Carregar a imagem
    print(path)
    imagem = cv2.imread(path)
 
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    if (antigo is not None):
        diferenca = cv2.absdiff(gray, antigo)
        #corrige mudanças de iluminação em todas as imagens
        diferenca = cv2.threshold(diferenca, 110, 255, cv2.THRESH_BINARY)[1] 
                
        #print(diferenca)
        cv2.imshow('Imagem', diferenca)
        
    antigo = gray
    
    # Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print("Erro ao carregar a imagem")
    

# Crie uma janela chamada 'Imagem'
cv2.namedWindow('Imagem')

# Crie uma trackbar chamada 'i' na janela 'Imagem'
cv2.createTrackbar('i', 'Imagem', 0, 12, on_trackbar_change)

on_trackbar_change(0)

cv2.waitKey()



cv2.destroyAllWindows()  # Fechar todas as janelas abertas
