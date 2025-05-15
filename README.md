# FIAP - Faculdade de Informática e Administração Paulista  
## Enterprise Challenge - Sprint 1 — Hermes Reply  

*Grupo 13*  
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

### Diagrama de Componentes

> [Inserir imagem do diagrama de componentes aqui]  

### Diagrama de Sequência — Fluxo Principal

> [Inserir imagem do diagrama de sequência aqui]  

### Jornada de Uso — Exemplo “Metalúrgica X”

1. *Onboarding e cadastro* de usuários no tenant "Metalúrgica X"
2. *Integração dos sensores* com a plataforma via MQTT
3. *Configuração de regras* e *visualização de dashboards*
4. *Detecção de anomalias* com recomendações automáticas
5. *Aprimoramento contínuo* dos modelos via SageMaker

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

# (Dependendo do módulo, execute os passos específicos)




