from comparador_de_matrices import comparar_dos_imagenes
from operator import itemgetter

def extraer_coincidencia_entre_series(serie_actual,series_antiguas):
        
        contador = 0
        lista_series_y_similitud = []
        barra_de_carga = 0
        
        try:

            print ("Comparando las " + str(len(series_antiguas)) + " series disponibles.")

            for serie_antigua in series_antiguas:

                barra_de_carga = barra_de_carga +1
                porcentaje = (barra_de_carga / (len(series_antiguas))) *100
        
                print(" Comparando serie : " + (str(barra_de_carga)) + "/" + (str(len(series_antiguas))) + " (" + (str(round(porcentaje))) + "%)")

                sumatorio_de_diferencias_de_una_serie = 0

                if len(serie_antigua) == len(serie_actual):
                    
                    for contador in range(len(serie_actual)):
            
                        imagen_antigua = (serie_antigua[contador])
                        imagen_actual = (serie_actual[contador])
                            
                        diferencia = (comparar_dos_imagenes(imagen_actual,imagen_antigua,False,0))

                        sumatorio_de_diferencias_de_una_serie = sumatorio_de_diferencias_de_una_serie + diferencia

                    lista_series_y_similitud.append((serie_actual,serie_antigua,sumatorio_de_diferencias_de_una_serie))
                    
                else:
                    print("Las series a comparar tienen que tener la misma longitud")

                """ Ordenamos de mayor similitud a menor similitud """
                lista_series_y_similitud = sorted(lista_series_y_similitud, key=itemgetter(2))

            return lista_series_y_similitud
        
        except: TypeError