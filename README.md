# 💡 Challenge Reply – Prevenção de Falhas em Motores Industriais

## 🧠 Justificativa do Problema

Na indústria 4.0, paradas inesperadas causadas por falhas em motores industriais são um dos maiores vilões da produtividade. Vibrações anormais, superaquecimento ou desgaste de rolamentos geralmente não são percebidos até que o problema se agrave, gerando prejuízos operacionais e financeiros.

Antecipar essas falhas, por meio de sensores e análise preditiva, é essencial para aumentar a eficiência e reduzir custos com manutenção corretiva.

## 💡 Descrição da Solução Proposta

Esta proposta visa o desenvolvimento de uma solução digital para monitoramento em tempo real de motores industriais utilizando sensores de vibração conectados a ESP32. Os dados serão enviados para a nuvem, processados por modelos de Machine Learning e exibidos em dashboards com alertas inteligentes.

A proposta contribui diretamente para a manutenção preditiva, aumento da vida útil dos equipamentos e redução de custos com falhas inesperadas.

## 🧰 Tecnologias Utilizadas

| Categoria | Tecnologias |
|----------|-------------|
| Linguagem principal | Python |
| Bibliotecas de IA | Scikit-learn, Pandas, NumPy |
| Armazenamento | PostgreSQL (RDS da AWS – simulado) |
| Coleta de dados | ESP32 + sensor de vibração (simulado) |
| Comunicação | MQTT (simulado) |
| Processamento | AWS EC2 (simulado) |
| Visualização | Dash ou Streamlit |
| Arquitetura | Diagrama com diagrams.net |

## 🔄 Pipeline de Dados

1. **Coleta de Dados:** Sensor de vibração coleta dados dos motores via ESP32;
2. **Transmissão:** Dados enviados via MQTT para o servidor;
3. **Armazenamento:** Dados salvos em um banco de dados PostgreSQL;
4. **Processamento:** Scripts em Python processam os dados e alimentam o modelo de Machine Learning;
5. **Predição:** Modelo identifica padrões de falhas com base no histórico;
6. **Visualização:** Dashboards exibem status dos motores, alertas e métricas.

## 🧱 Arquitetura da Solução

*(Inserir o diagrama aqui - veja abaixo como gerar)*

## 🗂️ Plano Inicial de Desenvolvimento

| Integrante | Responsabilidade |
|-----------|------------------|
| Amanda | Organização geral, documentação e GitHub |
| Integrante 2 | Simulação da coleta de dados com ESP32 e MQTT |
| Integrante 3 | Processamento dos dados e aplicação do modelo de ML |
| Integrante 4 | Construção do dashboard e alertas inteligentes |
| Integrante 5 (opcional) | Diagrama da arquitetura e suporte na integração |

## 📌 Observações

- Dados simulados foram utilizados nesta fase;
- O objetivo é propor uma solução coerente e viável, não um MVP funcional;
- As decisões técnicas foram fundamentadas em boas práticas e escalabilidade futura.

---

## 📎 Diagrama da Arquitetura

[Clique aqui para abrir o diagrams.net](https://app.diagrams.net/)

Elementos recomendados:
- **ESP32 + sensor de vibração**
- **Broker MQTT**
- **Servidor EC2 (Python + ML)**
- **Banco de Dados RDS**
- **Dashboards com alertas**

---


