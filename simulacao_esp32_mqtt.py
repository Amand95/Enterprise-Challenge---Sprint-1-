# simulacao_esp32_mqtt.py
# Simulação da coleta de dados de vibração com ESP32 e envio via MQTT
# Projeto: Challenge Reply – Prevenção de Falhas em Motores Industriais (Grupo 13 - FIAP)

import random
import time
import paho.mqtt.client as mqtt
import json
import datetime

# Configurações do broker MQTT público
broker = "test.mosquitto.org"
port = 1883
topic = "fiap/desafio/vibracao"

# Cria cliente MQTT e configura os callbacks
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

client.on_connect = on_connect
client.on_publish = on_publish

# Conecta ao broker MQTT
client.connect(broker, port)
client.loop_start()

print("🚀 Iniciando simulação de envio de dados de vibração...\n(Pressione CTRL+C para encerrar)\n")

try:
    while True:
        # Gera um valor aleatório de vibração (em mm/s)
        vibracao = round(random.uniform(0.2, 4.5), 2)
        timestamp = datetime.datetime.now().isoformat()

        # Cria a mensagem no formato JSON
        mensagem = json.dumps({
            "vibracao": vibracao,
            "timestamp": timestamp
        })

        # Publica a mensagem no tópico MQTT
        result = client.publish(topic, mensagem)
        status = result.rc

        if status == mqtt.MQTT_ERR_SUCCESS:
            print(f"📡 Enviado para {topic}: {mensagem}")
        else:
            print("⚠️ Falha ao enviar a mensagem.")

        # Aguarda 5 segundos antes de enviar novamente
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Simulação encerrada manualmente.")
except Exception as e:
    print(f"❗ Erro durante a simulação: {e}")
finally:
    client.loop_stop()
    client.disconnect()
    print("🔌 Conexão com o broker encerrada.")
