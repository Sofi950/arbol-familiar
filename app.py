# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Sofia" # escribe tu nombre
    age = "16" # escribe tu edad

    return render_template('index.html' , name = name , age = age)
emo_code_url = {

 "father": [0, "./static/father.png"],
 "friend": [1, "./static/friend.png"],
 "me": [2, "./static/me.png"],
 "mother": [3, "./static/mother.png"],

}

# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)
