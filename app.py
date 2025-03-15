from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    resultado_nombre = None
    resultado_mensaje = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        mensaje = request.form['mensaje']

        if nombre and mensaje:
            resultado_nombre = nombre
            resultado_mensaje = mensaje
        else:
            mensaje = "Por favor, completa todos los campos."

    # Si es una solicitud GET, los resultados son None
    return render_template('index.html', mensaje=mensaje, resultado_nombre=resultado_nombre, resultado_mensaje=resultado_mensaje)

if __name__ == '__main__':
    app.run(debug=True)