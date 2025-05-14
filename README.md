# FIAP - Faculdade de Informática e Administração Paulista

## Nome do Projeto: Challenge Reply – Prevenção de Falhas em Motores Industriais

## Nome do Grupo: Grupo 13

👨‍🎓 **Integrantes**:
- Amanda da Silva Barros
- Karina Jesus dos Santos
- João Victor Cope Moreira

## 🧠 Justificativa do Problema
Na Indústria 4.0, falhas inesperadas em motores industriais são uma das principais causas de paradas de produção, resultando em grandes perdas financeiras e operacionais. Muitas falhas, como vibrações anormais, superaquecimento ou desgaste de rolamentos, não são percebidas até que o problema se agrave, levando a manutenções corretivas caras e períodos de inatividade prolongados.

A antecipação de falhas é crucial para melhorar a eficiência e reduzir custos. Utilizando sensores de vibração e análise preditiva, é possível identificar sinais de falhas antes que ocorram, permitindo a implementação de manutenção preditiva. Isso aumenta a vida útil dos equipamentos, reduz a necessidade de manutenção corretiva e melhora a produtividade da fábrica.

## 💡 Descrição da Solução Proposta
Este projeto propõe o desenvolvimento de uma solução digital para o monitoramento em tempo real de motores industriais, utilizando sensores de vibração conectados a um ESP32. Os dados coletados pelos sensores serão enviados para a nuvem, processados por modelos de Machine Learning (ML) e apresentados em dashboards com alertas inteligentes.

A solução vai ajudar na manutenção preditiva, prevendo falhas antes que se tornem problemas graves, otimizando os processos e reduzindo custos com paradas inesperadas.

## 🧰 Tecnologias Utilizadas

| **Categoria**        | **Tecnologias**                                                   |
|----------------------|--------------------------------------------------------------------|
| **Linguagem principal** | Python                                                           |
| **Bibliotecas de IA**   | Scikit-learn, Pandas, NumPy                                      |
| **Armazenamento**       | PostgreSQL (RDS da AWS – simulado)                                |
| **Coleta de dados**    | ESP32 + Sensor de Vibração (simulado)                             |
| **Comunicação**        | MQTT (simulado)                                                   |
| **Processamento**      | AWS EC2 (simulado)                                                |
| **Visualização**       | Dash ou Streamlit                                                 |
| **Arquitetura**        | Diagrama com diagrams.net                                          |

## 🔄 Pipeline de Dados
1. **Coleta de Dados**: Sensores de vibração coletam dados dos motores industriais via ESP32.
2. **Transmissão**: Os dados são enviados via MQTT para o servidor na nuvem.
3. **Armazenamento**: Os dados são armazenados em um banco de dados PostgreSQL, usando RDS da AWS (simulado).
4. **Processamento**: Scripts em Python processam os dados e alimentam o modelo de Machine Learning.
5. **Predição**: O modelo de Machine Learning identifica padrões de falhas com base no histórico de dados.
6. **Visualização**: Dashboards são gerados para exibir o status dos motores, alertas e métricas de performance.

## 🧱 Arquitetura da Solução
A arquitetura proposta é composta por vários componentes interconectados que permitem a coleta, transmissão, armazenamento, processamento e visualização dos dados de vibração. Abaixo, encontra-se o diagrama da arquitetura:

**Componentes da Arquitetura**:
- **ESP32 + Sensor de Vibração**: Coleta e transmite dados de vibração dos motores.
- **MQTT**: Protocolo de comunicação para enviar os dados para o servidor.
- **AWS EC2**: Responsável pelo processamento dos dados e execução dos modelos de Machine Learning.
- **PostgreSQL (RDS da AWS)**: Banco de dados para armazenamento dos dados coletados.
- **Dash/Streamlit**: Utilizados para criar os dashboards e exibir os resultados da análise.

## 🗂️ Plano Inicial de Desenvolvimento

| **Integrante**    | **Responsabilidade**                                                      |
|-------------------|---------------------------------------------------------------------------|
| **Amanda**        | Organização geral, documentação e GitHub                                 |
| **Amanda**        | Simulação da coleta de dados com ESP32 e MQTT                             |
| **João**          | Processamento dos dados e aplicação do modelo de Machine Learning (ML)     |
| **Karina**        | Construção do dashboard e alertas inteligentes                            |
| **João**          | Diagrama da arquitetura e suporte na integração                           |

## 📌 Observações
- Dados simulados foram utilizados nesta fase do projeto.
- O objetivo desta entrega não é um MVP funcional, mas sim a definição de uma arquitetura coerente e viável.
- A proposta considera boas práticas e a escalabilidade do projeto para fases futuras.
- A solução considera um modelo de Machine Learning que pode ser expandido no futuro para maior precisão nas previsões.
- O uso de sensores e a coleta de dados são simulados, pois o foco nesta fase é na definição da estrutura e não na implementação física.

## 📎 Diagrama da Arquitetura
A arquitetura foi desenhada com a ferramenta diagrams.net. Este diagrama ilustra todos os componentes da solução e a interconexão entre eles.

## 🔗 Repositório GitHub
O repositório GitHub foi estruturado para seguir as melhores práticas de desenvolvimento colaborativo. O link para o repositório é privado e foi compartilhado com os tutores para a avaliação.

## 📅 Cronograma de Desenvolvimento

1. **Fase 1 (Definição da Arquitetura e Tecnologias)**:
   - Coleta e definição de tecnologias: 1 semana
   - Escolha do banco de dados e serviços em nuvem: 2 dias

2. **Fase 2 (Desenvolvimento da Pipeline e Processamento de Dados)**:
   - Implementação da coleta de dados e MQTT: 1 semana
   - Processamento de dados e integração com ML: 1 semana

3. **Fase 3 (Construção de Dashboards e Implementação dos Alertas)**:
   - Desenvolvimento dos dashboards: 1 semana
   - Testes de alertas e integração com os dados: 1 semana

## ⚙️ Como Rodar a Solução
Para rodar o projeto localmente ou em um servidor, siga as instruções abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Amand95/Enterprise-Challenge---Sprint-1-.git



