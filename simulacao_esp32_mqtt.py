import random
import time
import json
import datetime
import paho.mqtt.client as mqtt
import threading

# Configurações do broker MQTT público
broker = "test.mosquitto.org"
port = 1883
topic = "fiap/desafio/vibracao"

# Função de callback para quando a conexão com o broker for estabelecida
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao broker MQTT com sucesso!")
    else:
        print(f"❌ Falha na conexão. Código de retorno: {rc}")
    # Subscreve ao tópico após conectar
    client.subscribe(topic)

# Função de callback para quando uma mensagem for publicada
def on_publish(client, userdata, mid):
    print(f"📤 Mensagem publicada com sucesso. ID: {mid}")

# Função para simular a coleta e envio de dados
def simulate_data():
    while True:
        try:
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

        except Exception as e:
            print(f"❗ Erro na simulação: {e}")
            time.sleep(5)

# Função para garantir a reconexão automática em caso de desconexão
def on_disconnect(client, userdata, rc):
    print("❌ Desconectado do broker. Tentando reconectar...")
    while rc != 0:
        try:
            client.reconnect()
            print("✅ Reconexão bem-sucedida!")
        except:
            print("⚠️ Falha na reconexão. Tentando novamente em 5 segundos.")
            time.sleep(5)

# Criação e configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Conectar ao broker MQTT
client.connect(broker, port)
client.loop_start()

# Inicia a simulação em uma thread separada para não bloquear a execução
simulator_thread = threading.Thread(target=simulate_data)
simulator_thread.daemon = True
simulator_thread.start()

# Aguarda o encerramento do programa
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Simulação encerrada manualmente.")
    client.disconnect()
    client.loop_stop()
