from PIL import Image
import os
from handler_s3_images import download_images_small


def comparar_dos_imagenes(imagen_actual,imagen_antigua,guarda_imagen,n):


    """Evita que descargue imagenes ya descargadas para agilizar"""

    if imagen_actual not in os.listdir("images_small/"):
        download_images_small(imagen_actual)

    if imagen_antigua not in os.listdir("images_small/"):
        download_images_small(imagen_antigua)


    path_1 = "images_small/" + imagen_actual

    path_2 = "images_small/" + imagen_antigua

    #carga de las imagenes
    
    imagen1 = Image.open(path_1)

    imagen2 = Image.open(path_2)
    
    #obtencion de los datos de ambas imagenes

    datos_imagen1 = imagen1.getdata()

    datos_imagen2 = imagen2.getdata()

    """calculo de diferencias"""
    
    datos_diferencias = [abs(datos_imagen1[x]-datos_imagen2[x]) for x in range(len(datos_imagen1))]

    """saca un valor total sumando la diferencia de todos los píxeles."""

    def recorre_y_suma_las_diferencias_de_cada_pixel(datos_diferencias):
                            
                            sumatorio = 0

                            tamaño_imagen = len(datos_diferencias)

                            """ El pie de la foto contiene información cambiante que altera la comparación"""
                            imagen_a_recortar = tamaño_imagen * 0.9

                            for idx,fila in enumerate(datos_diferencias):
                                """ Recortamos parte util superior """
                                if idx < imagen_a_recortar:    
                                    sumatorio = sumatorio + fila
                                
                            return sumatorio


    diferencia_numerica = (recorre_y_suma_las_diferencias_de_cada_pixel(datos_diferencias))
 
    """creacion de la nueva imagen con las diferencias mapeadas"""
    
    imagen_diferencias = Image.new('L', imagen1.size)
    
    imagen_diferencias.putdata(datos_diferencias)
    
    if guarda_imagen:
        imagen_diferencias.save("static/diferencias-" + str(n) + ".png" )
    
    imagen1.close() 
    imagen2.close()
    
    imagen_diferencias.close()



    return diferencia_numerica