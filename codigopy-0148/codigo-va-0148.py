# Importamos las librerías
import cv2
import matplotlib.pyplot as plt
import os 
# ruta de la imagen
ruta_imagen = os.path.join(
    "img-original-0148",
    "img-pinguino-0148.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
pinguino = cv2.imread(ruta_imagen)
# print(Pinguino) muestra las matrices de la imagen
# # Convertir de BGR a RGB color rojo COLOR_BGR2RGB
Pingu = cv2.cvtColor(pinguino, cv2.COLOR_BGR2RGB)
# cv2.imshow("Mochila original",pinguino)
cv2.imshow("Pinguino color 0148", Pingu)
cv2.waitKey(0) # Tiempo de espera 
cv2.destroyAllWindows() # Destruye todas las ventanas en memoria