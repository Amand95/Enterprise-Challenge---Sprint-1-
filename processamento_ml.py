import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Carrega os dados do arquivo CSV
dados = pd.read_csv('dados_vibracao.csv')

# Exibe as primeiras linhas do arquivo para inspecionar os dados
print(dados.head())

# Verificando se há dados ausentes
print("\nVerificando dados ausentes:")
print(dados.isnull().sum())

# Processamento do dado - Convertendo o timestamp para um formato numérico (ex: timestamp unix)
dados['timestamp'] = pd.to_datetime(dados['timestamp'])
dados['timestamp'] = dados['timestamp'].apply(lambda x: x.timestamp())

# Adiciona uma coluna para a classificação (ex: falha se vibração > 3.0, normal caso contrário)
dados['classe'] = np.where(dados['vibracao'] > 3.0, 'falha', 'normal')

# Exibe as primeiras linhas do arquivo após a transformação
print("\nDados após transformação:")
print(dados.head())

# Visualizando a distribuição das classes
dados['classe'].value_counts().plot(kind='bar', title='Distribuição de Classes (Falha vs Normal)')
plt.xlabel('Classe')
plt.ylabel('Contagem')
plt.show()

# Definindo variáveis independentes (X) e dependente (y)
X = dados[['timestamp', 'vibracao']]
y = dados['classe']

# Dividindo os dados em treinamento e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializando o modelo de Árvore de Decisão
modelo = DecisionTreeClassifier(random_state=42)

# Treinando o modelo
modelo.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
y_pred = modelo.predict(X_test)

# Avaliando o modelo
print("\nAcurácia do Modelo:")
print(accuracy_score(y_test, y_pred))

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

print("\nMatriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

# Visualizando a importância das variáveis
importances = modelo.feature_importances_
features = X.columns

# Plotando a importância das variáveis
plt.barh(features, importances)
plt.title('Importância das Variáveis')
plt.xlabel('Importância')
plt.ylabel('Variáveis')
plt.show()
