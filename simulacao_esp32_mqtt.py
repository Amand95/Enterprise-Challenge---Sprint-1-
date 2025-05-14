# simulacao_esp32_mqtt.py
# Simulação da coleta de dados de vibração com ESP32 e envio via MQTT
# Projeto: Challenge Reply – Prevenção de Falhas em Motores Industriais (Grupo 13 - FIAP)

import random
import time
import paho.mqtt.client as mqtt

# Configurações do broker MQTT público
broker = "test.mosquitto.org"
port = 1883
topic = "fiap/desafio/vibracao"

# Cria cliente MQTT e conecta ao broker
client = mqtt.Client()
client.connect(broker, port)

print("Iniciando simulação de envio de dados de vibração...")

try:
    while True:
        # Gera um valor aleatório de vibração (em mm/s)
        vibracao = round(random.uniform(0.2, 4.5), 2)
        mensagem = f'{{"vibracao": {vibracao}}}'

        # Publica a mensagem no tópico MQTT
        client.publish(topic, mensagem)
        print(f"Publicado no tópico {topic}: {mensagem}")

        # Aguarda 5 segundos antes de enviar novamente
        time.sleep(5)

except KeyboardInterrupt:
    print("Simulação encerrada manualmente.")
    client.disconnect()

