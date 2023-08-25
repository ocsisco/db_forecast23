import os
from handler_s3_images import s3_images_list

def extraer_series_antiguas(longitud_de_la_serie,descarte):

      
    files_names = s3_images_list()
    files_names = sorted(files_names)
    series = []
    files_names = list(files_names)

    try:

        
        for idx in range(len(files_names)):

            """Evita que cuando idx llega al final de la lista no se puedan crear idx+posicion ya que se encuentran fuera de la lista"""
            if idx <= (len(files_names)-longitud_de_la_serie):

                serie = []
                            
                for posicion in range(longitud_de_la_serie):       
                
                    captura_actual = files_names[idx + posicion]

                    serie.append(captura_actual)

                series.append(serie)

        """El descarte son la cantidad de imagenes que desprecia al crear la lista, ya que las imagenes inmediatamente anteriores a las actuales son, generalmente, las mas similares del historico."""
        for n in range(descarte):
            series.pop()
                                           
        return series
    
    except: IndexError


