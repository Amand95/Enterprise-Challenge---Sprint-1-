import random
import time
import json
import datetime
import paho.mqtt.client as mqtt

# Configurações do broker MQTT público
broker = "test.mosquitto.org"
port = 1883
topic = "fiap/desafio/vibracao"

# Função de callback para quando a conexão for estabelecida
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao broker MQTT com sucesso!")
    else:
        print(f"❌ Falha na conexão. Código de retorno: {rc}")

# Função de callback para quando a mensagem for publicada com sucesso
def on_publish(client, userdata, mid):
    print(f"📤 Mensagem publicada com sucesso. ID: {mid}")

# Função para configurar e conectar o cliente MQTT
def connect_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    try:
        client.connect(broker, port)
        client.loop_start()  # Inicia o loop do cliente MQTT
        return client
    except Exception as e:
        print(f"❗ Erro ao conectar ao broker: {e}")
        return None

# Função para gerar e enviar dados de vibração
def send_vibration_data(client):
    print("🚀 Iniciando simulação de envio de dados de vibração...\n(Pressione CTRL+C para encerrar)\n")
    
    try:
        while True:
            # Gera um valor aleatório de vibração (em mm/s)
            vibracao = round(random.uniform(0.2, 4.5), 2)
            timestamp = datetime.datetime.now().isoformat()

            # Cria a mensagem em formato JSON
            mensagem = json.dumps({
                "vibracao": vibracao,
                "timestamp": timestamp
            })
            
            # Publica a mensagem no tópico MQTT
            result = client.publish(topic, mensagem)
            status = result.rc  # Verifica o status da publicação
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
        # Finaliza a conexão com o broker
        client.loop_stop()
        client.disconnect()
        print("🔌 Conexão com o broker encerrada.")

# Função principal para iniciar a simulação
def main():
    client = connect_mqtt()
    if client:
        send_vibration_data(client)
    else:
        print("Falha na conexão com o broker MQTT. A simulação não foi iniciada.")

# Executa o script principal
if __name__ == "__main__":
    main()
