from flask import Flask, render_template, request
import joblib
import numpy as np
import os

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo entrenado desde la carpeta del venv (S4)
modelo_path = os.path.join(os.path.dirname(__file__), 'modelo_entrenado.pkl')
modelo = joblib.load(modelo_path)

# Ruta para la página principal con el formulario
@app.route('/')
def formulario():
    return render_template('formulario.html')

# Ruta para procesar las predicciones
@app.route('/predecir', methods=['POST'])
def predecir():
    if request.method == 'POST':
        # Obtener los valores del formulario
        pclass = int(request.form['pclass'])
        sex = int(request.form['sex'])  # 0 para female, 1 para male
        age = float(request.form['age'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])
        fare = float(request.form['fare'])
        embarked = int(request.form['embarked'])  # 0 = C, 1 = Q, 2 = S

        # Crear un array con los valores
        valores_entrada = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

        # Realizar la predicción
        prediccion = modelo.predict(valores_entrada)

        # Convertir la predicción a una respuesta
        resultado = 'Sobrevivió' if prediccion[0] == 1 else 'No sobrevivió'

        return render_template('resultado.html', resultado=resultado)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)