from comparador_de_matrices import comparar_dos_imagenes
from PIL import Image
from handler_s3_images import download_images_color,s3_images_list
import os


def extrae_resultados_a_static(series_y_similitud,longitud_serie_prevision):

    try:


        """ Extraemos el par de series con mayor similitud entre ellas"""
        top_menor_diferencia = (series_y_similitud[0])

        print(" ")
        print("Serie actual:                " + str(top_menor_diferencia[0]))
        print("Serie antigua mas similar:   " + str(top_menor_diferencia[1]))
        print("Grado diferencial total:     " + str(top_menor_diferencia[2]))
        print(" ")


        """ Borramos las imagenes para crear las nuevas ya que la serie puede cambiar de tamaño y no basta con escribir encima"""
        for file in os.listdir("static"):
            os.remove(os.path.join("static",file))   


        """ Recorremos el nombre de las imagenes de la serie antigua y guardamos una copia de su clon de color de la serie antigua, y de la actual """
        posicion_en_serie = 0

        for imagenes_antiguas in top_menor_diferencia[1]:
            
            download_images_color(imagenes_antiguas)
            imagen0 = Image.open("images_color/" + imagenes_antiguas)
            imagen0.save("static/comparacion-serie-antigua" + "-" + str(posicion_en_serie) + ".png")
            imagen0.close()
            posicion_en_serie = posicion_en_serie +1


        posicion_en_serie = 0

        for imagenes_actuales in top_menor_diferencia[0]:

            download_images_color(imagenes_actuales)
            imagen0 = Image.open("images_color/" + imagenes_actuales)
            imagen0.save("static/comparacion-serie-actual" + "-" + str(posicion_en_serie) + ".png")
            imagen0.close()
            posicion_en_serie = posicion_en_serie +1

        
        """y tambien las imagenes resultante de su comparación"""

        num_of_compares = len(top_menor_diferencia[0])
        for n in range(num_of_compares):
            
            imagen_actual = top_menor_diferencia[0][n]
            imagen_antigua = top_menor_diferencia[1][n]

            comparar_dos_imagenes(imagen_actual,imagen_antigua,True,n)

            
            print("Grado diferencial " + str(n) + ": " + str(comparar_dos_imagenes(imagen_actual,imagen_antigua,False,n)))


        
        """Tambien la serie posterior que se tomará como previsión"""

        imagen_de_referencia = top_menor_diferencia[1]
        imagen_de_referencia = imagen_de_referencia[-1]
        
        print(imagen_de_referencia)

        lista_de_imagenes = s3_images_list()

        index = lista_de_imagenes.index(imagen_de_referencia)
        prevision = []

        for posicion_en_serie in range(longitud_serie_prevision):
            prevision.append(lista_de_imagenes[index + posicion_en_serie +1])
            imagen = lista_de_imagenes[index + posicion_en_serie +1]

            download_images_color(imagen)
            imagen0 = Image.open("images_color/" + imagen)
            imagen0.save("static/prevision" + "-" + str(posicion_en_serie) + ".png")
            imagen0.close()

            

        


        print("")
        print ("Previsión basada en la serie posterior a la serie mas similar: " + str(prevision))
        print("_____________________________")

        print("_____________________________")

    except:IndexError
          
