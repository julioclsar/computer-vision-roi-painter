import cv2 as cv

img = cv.imread('robot.jpg')

linhas, colunas, canais = img.shape

print('Escala:', linhas, colunas)

codpix1 = int(input('Digite a coordenada: '))
codpix2 = int(input('Digite a coordenada: '))
codpix3 = int(input('Digite a coordenada: '))
codpix4 = int(input('Digite a coordenada: '))

img[codpix1:codpix3, codpix2:codpix4] = [0, 255, 0]

cv.imshow('Imagem', img)
cv.waitKey(0)