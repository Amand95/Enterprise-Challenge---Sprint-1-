import random
import time
import json
import datetime
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Configurações do broker MQTT
broker = "test.mosquitto.org"
port = 1883
topic = "fiap/desafio/vibracao"

# Inicializa o cliente MQTT
client = mqtt.Client()

# Callback para conexão
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao broker MQTT com sucesso!")
    else:
        print(f"❌ Falha na conexão. Código de retorno: {rc}")
        
# Callback para publicação
def on_publish(client, userdata, mid):
    print(f"📤 Mensagem publicada com sucesso. ID: {mid}")

# Função para gerar dados simulados
def gerar_dados():
    # Gera um valor aleatório de vibração (em mm/s)
    vibracao = round(random.uniform(0.2, 4.5), 2)
    timestamp = datetime.datetime.now().isoformat()
    
    # Classifica os dados em 'falha' ou 'normal'
    if vibracao > 3.0:
        status = 1  # 'Falha'
    else:
        status = 0  # 'Normal'

    # Cria e retorna a mensagem no formato JSON
    return json.dumps({
        "vibracao": vibracao,
        "status": status,
        "timestamp": timestamp
    })

# Função para treinar e salvar o modelo de ML
def treinar_modelo(dados):
    # Cria DataFrame para os dados de vibração
    df = pd.DataFrame(dados, columns=['vibracao', 'status'])

    # Separando variáveis independentes e dependentes
    X = df[['vibracao']]
    y = df['status']

    # Dividindo os dados para treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinando o modelo Random Forest
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Avaliando o modelo
    y_pred = modelo.predict(X_test)
    print("\nDesempenho do modelo:")
    print(classification_report(y_test, y_pred))

    # Matriz de Confusão
    cm = confusion_matrix(y_test, y_pred)
    print("\nMatriz de Confusão:")
    print(cm)

    # Salvando o modelo treinado
    joblib.dump(modelo, 'modelo_vibracao.pkl')
    print("✅ Modelo treinado e salvo com sucesso.")

# Função para visualizar dados
def visualizar_dados(dados):
    df = pd.DataFrame(dados, columns=['vibracao', 'status'])
    
    # Histograma para visualizar a distribuição de vibração
    plt.figure(figsize=(10, 6))
    df['vibracao'].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribuição da Vibração')
    plt.xlabel('Vibração (mm/s)')
    plt.ylabel('Frequência')
    plt.show()

    # Gráfico de barras para visualizar status
    plt.figure(figsize=(8, 5))
    df['status'].value_counts().plot(kind='bar', color='lightcoral')
    plt.title('Distribuição de Status (Falha/Normal)')
    plt.xlabel('Status')
    plt.ylabel('Contagem')
    plt.xticks([0, 1], ['Normal', 'Falha'], rotation=0)
    plt.show()

# Callback para processamento de dados de vibração
def on_message(client, userdata, msg):
    # Recebe os dados do MQTT
    dados = json.loads(msg.payload)
    vibracao = dados['vibracao']
    status = dados['status']
    timestamp = dados['timestamp']
    
    # Exibe os dados recebidos
    print(f"🔴 Dado recebido - Vibração: {vibracao}mm/s | Status: {'Falha' if status == 1 else 'Normal'} | Timestamp: {timestamp}")
    
    # Adiciona os dados em uma lista para análise
    dados_armazenados.append([vibracao, status])

    # Visualiza os dados de tempos em tempos
    if len(dados_armazenados) % 100 == 0:
        visualizar_dados(dados_armazenados)

# Função principal para rodar a simulação
def executar_simulacao():
    # Inicializa a lista de dados simulados
    dados_armazenados = []

    # Configura o cliente MQTT
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message

    # Conecta ao broker MQTT
    client.connect(broker, port)
    client.loop_start()

    # Inscreve-se no tópico para receber dados
    client.subscribe(topic)

    try:
        while True:
            # Gera dados simulados e publica
            mensagem = gerar_dados()
            client.publish(topic, mensagem)
            print(f"📡 Publicado no tópico {topic}: {mensagem}")
            time.sleep(5)  # Aguarda 5 segundos antes de enviar novamente
            
    except KeyboardInterrupt:
        print("Simulação encerrada manualmente.")
        client.loop_stop()

# Rodando a simulação e treinando o modelo
if __name__ == "__main__":
    executar_simulacao()
    # Após coletar dados suficientes, treina o modelo
    if len(dados_armazenados) > 100:
        treinar_modelo(dados_armazenados)

