from extractor_imagenes_radar import captura_gif_de_la_fuente
from extractor_serie_actual import extraer_serie_actual
from extractor_series_antiguas import extraer_series_antiguas
from extractor_coincidencia_de_series import extraer_coincidencia_entre_series
from extractor_de_resultados_a_static import extrae_resultados_a_static
from remove_temp_files import remove_temp_files


import time
from datetime import datetime



"""

Longitud de la serie = longitud de la series que se van a comparar entre si.
Longitud de la serie previsión = cantidad de imagenes consecutivas siguientes a la serie mas similar, se usa como predicción.
Descarte = con toda probabilidad la serie mas parecida a la actual es la actual y con mucha probabilidad la serie anterior a la actual será la mas coicidente,
        de este modo se descartan en comparación tantas capturas como se desee (una captura son 10 minutos)

"""
longitud_de_la_serie = 3
longitud_serie_prevision = 6
descarte = 7


def obtencion_de_datos():

    while 1:
        
        tempus = datetime.now()
        tempus = tempus.minute

        if tempus == 1 or tempus == 11 or tempus == 21 or tempus == 31 or tempus == 41 or tempus == 51:
        

        
        
        
            #captura_gif_de_la_fuente("Zaragoza")
            #captura_gif_de_la_fuente("Almería")         
            #captura_gif_de_la_fuente("Asturias")       
            #captura_gif_de_la_fuente("Illes Balears")  
            #captura_gif_de_la_fuente("Barcelona")       
            #captura_gif_de_la_fuente("Cáceres")        
            #captura_gif_de_la_fuente("A Coruña")        
            #captura_gif_de_la_fuente("Madrid")          
            #captura_gif_de_la_fuente("Málaga")     
            #captura_gif_de_la_fuente("Murcia")          
            #captura_gif_de_la_fuente("Palencia")        
            #captura_gif_de_la_fuente("Las Palmas")      
            #captura_gif_de_la_fuente("Sevilla")         
            captura_gif_de_la_fuente("Valencia")        
            #captura_gif_de_la_fuente("Vizcaya")         
            #captura_gif_de_la_fuente("Zaragoza")

            
            serie_actual = extraer_serie_actual(longitud_de_la_serie)
            

            series_antiguas = extraer_series_antiguas(longitud_de_la_serie,descarte)
            

            series_y_similitud = extraer_coincidencia_entre_series(serie_actual,series_antiguas)
            

            extrae_resultados_a_static(series_y_similitud,longitud_serie_prevision)


            remove_temp_files()

                
            time.sleep(60)

