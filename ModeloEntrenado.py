# Importar bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Cargar el dataset
df = pd.read_csv(r"C:\Users\arhma\OneDrive\Escritorio\ActvS4\S4\Titanic.csv")  # Cambia la ruta por la ubicación de tu dataset

# Preprocesar los datos
# Eliminar columnas irrelevantes ('PassengerId', 'Name', 'Ticket', 'Cabin')
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

# Convertir la variable categórica 'Sex' a numérica
df['Sex'] = LabelEncoder().fit_transform(df['Sex'])

# Convertir la variable categórica 'Embarked' a numérica y manejar valores nulos
df['Embarked'] = LabelEncoder().fit_transform(df['Embarked'].fillna('S'))  # Reemplazar valores nulos con 'S'

# Manejar valores nulos en las columnas 'Age' y 'Fare'
imputer = SimpleImputer(strategy='median')
df[['Age', 'Fare']] = imputer.fit_transform(df[['Age', 'Fare']])

# Verificar si quedan valores nulos
print(df.isnull().sum())

# Separar las variables predictoras (X) y la variable objetivo (y)
X = df.drop('Survived', axis=1)
y = df['Survived']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Realizar predicciones
y_pred = rf_model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest accuracy: {accuracy * 100:.2f}%")

# Importancia de las características
importances = rf_model.feature_importances_
features = X.columns

# Mostrar la importancia de cada característica
plt.figure(figsize=(10, 6))
plt.barh(features, importances)
plt.xlabel('Importancia de las características')
plt.ylabel('Características')
plt.title('Importancia de las características en Random Forest')
plt.show()

# Guardar el modelo usando joblib
joblib.dump(rf_model, 'modelo_entrenado.pkl')
