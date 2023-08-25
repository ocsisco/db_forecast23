from flask import Flask,render_template,request
from multiprocessing import Process
import os
import shutil
from core import *

from handler_s3_images import s3_images_list,download_images_color






app = Flask(__name__)

if __name__ == "__main__":
    generate_images = Process(target=obtencion_de_datos)
    generate_images.start()
    print("principal")


@app.route('/ayuda')
def ayuda():
    return render_template("ayuda.html")

@app.route('/prevision')
def prevision():
    return render_template("prevision.html")

@app.route('/serie_actual')
def serie_actual():
    return render_template("serie_actual.html")

@app.route('/serie_antigua')
def serie_antigua():
    return render_template("serie_antigua.html")

@app.route('/historico_disponible')
def historico_disponible():

    lista_historico = []

    for file in s3_images_list():
        lista_historico.append(file)

    lista_historico = sorted(lista_historico)

    return str(lista_historico)



@app.route('/historico')
def historico():

    image_name = request.args.get("date")

    if "imagen.png" in os.listdir("static"):
          
        os.remove(os.path.join("static/imagen.png"))


    download_images_color(image_name)
    shutil.copy("images_color/" + image_name,"static/imagen.png")
    os.remove("images_color/" + image_name)
    

    print(image_name)
    
    
    return render_template("imagen_seleccionada.html",image_name=image_name)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=False)
