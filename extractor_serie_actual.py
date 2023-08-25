import os
from handler_s3_images import s3_images_list

def extraer_serie_actual(longitud_de_la_serie):

    try:
      
        serie = []

        files_names = s3_images_list()

        for longitud in range(longitud_de_la_serie):
                
            captura_actual = files_names[-longitud -1]

            serie.append(captura_actual)

        serie = sorted(serie)

        return serie
    
    except:IndexError

