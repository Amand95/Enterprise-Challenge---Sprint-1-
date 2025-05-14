# processamento_ml.py
import pandas as pd
import numpy as np
import random
import time
import paho.mqtt.client as mqtt
import json
import datetime
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt

# Configuração do broker MQTT
broker = "test.mosquitto.org"
port = 1883
topic = "fiap/desafio/vibracao"

# Criando cliente MQTT
client = mqtt.Client()
client.connect(broker, port)

# Função para simular a coleta de dados de vibração
def coleta_dados():
    vibracao = round(random.uniform(0.2, 4.5), 2)  # Gera valor aleatório de vibração
    timestamp = datetime.datetime.now().isoformat()  # Cria um timestamp
    mensagem = json.dumps({"vibracao": vibracao, "timestamp": timestamp})  # Cria mensagem em JSON
    return mensagem

# Função para criar um DataFrame simulando coleta de dados
def simula_dados():
    dados = []
    for _ in range(1000):  # Simula 1000 dados
        mensagem = coleta_dados()
        dados.append(json.loads(mensagem))
        time.sleep(0.1)
    return pd.DataFrame(dados)

# Função de pré-processamento dos dados
def preprocessamento(dados):
    dados['timestamp'] = pd.to_datetime(dados['timestamp'])  # Converte para datetime
    dados['vibracao'] = dados['vibracao'].fillna(dados['vibracao'].mean())  # Preenche valores ausentes com a média
    dados['falha'] = dados['vibracao'].apply(lambda x: 1 if x > 3.5 else 0)  # Marca como falha (1) ou normal (0)
    return dados[['vibracao']], dados['falha']  # Retorna as features e o target

# Função para treinar e avaliar o modelo
def treinar_modelo(X_train, y_train, X_test, y_test):
    modelo = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_leaf=4)  # Modelo ajustado
    modelo.fit(X_train, y_train)  # Treinamento

    # Previsões
    y_pred = modelo.predict(X_test)

    # Avaliação
    print("Acurácia do modelo:", accuracy_score(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))
    print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))

    # Salva o modelo treinado
    joblib.dump(modelo, 'modelo_vibracao.pkl')
    print("Modelo treinado salvo como 'modelo_vibracao.pkl'.")

    return modelo

# Função para visualizar os dados e a importância das variáveis
def visualizacao(dados, modelo):
    # Distribuição das classes (falha x normal)
    dados['falha'].value_counts().plot(kind='bar', title='Distribuição das Classes (Falha x Normal)', color=['green', 'red'])
    plt.xlabel('Classe')
    plt.ylabel('Contagem')
    plt.show()

    # Importância das variáveis
    feature_importances = modelo.feature_importances_
    plt.barh(['vibracao'], feature_importances, color='blue')
    plt.xlabel('Importância')
    plt.title('Importância das Variáveis')
    plt.show()

# Função principal para orquestrar todo o fluxo
def main():
    # Coleta de dados simulados
    dados = simula_dados()

    # Pré-processamento dos dados
    X, y = preprocessamento(dados)

    # Divisão entre dados de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalização dos dados
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Treinamento do modelo
    modelo = treinar_modelo(X_train, y_train, X_test, y_test)

    # Visualização
    visualizacao(dados, modelo)

    # Envio de dados simulados via MQTT
    while True:
        mensagem = coleta_dados()
        client.publish(topic, mensagem)
        print(f"Publicado: {mensagem}")
        time.sleep(5)

# Execução principal
if __name__ == '__main__':
    main()
