# FIAP - Faculdade de Informática e Administração Paulista  
## Enterprise Challenge - Sprint 1 — Hermes Reply  

**Grupo 13**  
- Amanda da Silva Barros  
- Lucas Fagundes  
- Karina Jesus dos Santos  
- João Victor Cope Moreira  
- Bruno Gambarini  

---

## Visão Geral

Este repositório documenta a solução desenvolvida para o desafio proposto pela Hermes Reply no contexto do Enterprise Challenge da FIAP. A proposta consiste em uma *plataforma SaaS de monitoramento industrial* com foco em *prevenção de falhas, visibilidade operacional e inteligência preditiva, utilizando **IoT, IA e análise de dados* em um cenário industrial.

---

## Objetivo da Solução

Desenvolver uma arquitetura escalável e segura que permita:

- Ingestão contínua de dados de sensores industriais via MQTT.  
- Processamento e enriquecimento de dados em tempo real.  
- Armazenamento eficiente de séries temporais e dados históricos.  
- Visualização de métricas e indicadores via dashboards interativos.  
- Detecção automática de anomalias e predição de falhas via IA.  
- Governança multi-tenant, com autenticação e trilhas de auditoria.  

---

## Tecnologias e Ferramentas

| Categoria             | Tecnologia/Ferramenta                      |  
|----------------------|--------------------------------------------|  
| Ingestão IoT         | AWS IoT Core (MQTT)                        |  
| Backend              | FastAPI (Python) + ECS Fargate             |  
| Armazenamento        | AWS Timestream, S3, PostgreSQL             |  
| ETL                  | AWS Glue                                   |  
| Data Warehouse       | Amazon Redshift                            |  
| Machine Learning     | Amazon SageMaker, AWS Bedrock              |  
| Front-end            | React 19 + Vite                            |  
| Autenticação         | Amazon Cognito                             |  
| Notificações         | Amazon SNS / SES                           |  
| Observabilidade      | AWS CloudWatch, Secrets Manager, Macie     |  

---

## Arquitetura da Solução

A arquitetura é composta pelos seguintes componentes principais:  
1. Ingestão de Dados: Sensores publicam dados via MQTT para o AWS IoT Core.  
2. Processamento: AWS Lambda valida, enriquece e roteia os dados.  
3. Armazenamento: Dados normalizados são armazenados no AWS Timestream; mensagens originais são arquivadas no Amazon S3.  
4. ETL: AWS Glue consolida dados de diferentes fontes e os grava no Amazon Redshift.  
5. Análise Operacional: Engine de analytics lê dados do Timestream e Redshift, avalia condições e envia alertas.  
6. Consumo: Usuários autenticados acessam dashboards em tempo real e relatórios históricos.

**Diagramas:**  
- Diagrama de Componentes  
- Diagrama de Sequência  
- Jornada de Uso - Exemplo “Metalúrgica X”  

---

## Principais Funcionalidades

- Cadastro de ativos industriais e hierarquias  
- Ingestão e normalização de telemetria  
- Dashboards operacionais em tempo real  
- Alertas inteligentes com regras configuráveis  
- Predição de falhas e estimativa de vida útil (RUL)  
- Recomendações automáticas via LLM (Bedrock)  

---

## Como Executar o Projeto

```bash
# Clone o repositório  
git clone https://github.com/olucasfagundes/fiap-enterprise-challenge-sprint-1.git  

# Acesse o diretório  
cd fiap-enterprise-challenge-sprint-1  

# Instale as dependências do backend  
cd src/backend  
pip install -r requirements.txt  

# Execute o backend  
uvicorn main:app --reload  

# Instale as dependências do frontend  
cd ../frontend  
npm install  

# Execute o frontend  
npm run dev  
