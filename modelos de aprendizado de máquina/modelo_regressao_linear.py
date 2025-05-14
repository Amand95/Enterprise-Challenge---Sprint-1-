import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Simulando dados
df = pd.read_csv('seu_arquivo.csv')

X = df[['N', 'P', 'K', 'temperatura', 'umidade', 'pH', 'precipitação']]
y = df['rótulo']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

erro = mean_squared_error(y_test, y_pred)
print(f'Erro quadrático médio: {erro}')
