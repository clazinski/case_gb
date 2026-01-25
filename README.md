# Case de Analytics Engineer — GB
Projeto para importar, transformar e modelar dados de vendas (2017-2019) utilizando GCP, Python e SQL.

## Objetivos da Implementação
- Carga e tratamento de dados
- Modelagem analítica
- Automação e versionamento
- Geração de insights para o time de negócio

## Estrutura

- /cloud_functions → código da função de ingestão para camada RAW
- sql_scripts/datasets → queries para criar tabelas

## Arquitetura do Fluxo de Dados
![Arquitetura proposta para o case.](https://i.postimg.cc/1m9vJRkV/arq.png)
Visão geral do processo de ingestão, tratamento e modelagem.

## Tech stack
- Google Cloud Storage
- Cloud Functions (Python)
- BigQuery
- BigQuery Scheduled Queries
- Cloud Scheduler
- Looker Studio

## Modelagem
```
                                                     ┌───────────────────────────────┐
                                                     │        staging.vendas         │
                                                     │-------------------------------│
                                                     │ data_venda          (DATE)    │
                                                     │ ano_venda           (INTEGER) │
                                                     | mes_venda           (INTEGER) │
                                                     | marca               (STRING)  │
                                                     | id_marca            (INTEGER) │
                                                     │ linha               (STRING)  │
                                                     | id_linha            (INTEGER) │
                                                     │ qtd_venda           (INTEGER) │
                                                     │ data_processamento (TIMESTAMP)│
                                                     └─────────────┬─────────────────┘
                                                                   │
        ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                              │                                  │                           │
┌───────────────────────────────┐  ┌───────────────────────────────────┐ ┌─────────────────────────────────┐ ┌────────────────────────────────┐
│ analytics.vendas_por_mes_ano  │  │ analytics.vendas_por_marca_linha  │ │ analytics.vendas_por_marca_data │ │ analytics.vendas_por_linha_data│
│-------------------------------│  │-----------------------------------│ │---------------------------------│ │--------------------------------│
│ data_venda         (DATE)     │  | id_marca               (INTEGER)  │ | id_marca           (INTEGER)    │ │ id_linha             (INTEGER) │
│ ano                (INTEGER)  │  | marca                  (STRING)   │ │ marca              (STRING)     │ │ linha                (STRING)  │
│ mes                (INTEGER)  │  | id_linha               (INTEGER)  │ │ data_venda         (DATE)       │ │ data_venda           (DATE)    │
│ total_vendas       (INTEGER)  │  │ linha                  (STRING)   │ | ano                (INTEGER)    | │ ano                  (INTEGER) │
│ total_registros    (INTEGER)  │  │ total_vendas           (INTEGER)  │ | mes                (INTEGER)    | │ mes                  (INTEGER) │
│ data_processamento (TIMESTAMP)│  │ total_registros        (INTEGER)  │ │ total_vendas       (INTEGER)    │ │ total_vendas         (INTEGER) │
└───────────────────────────────┘  │ data_processamento     (TIMESTAMP)│ │ total_registros    (INTEGER)    │ │ total_registros      (INTEGER) │
                                   └───────────────────────────────────┘ │ data_processamento (TIMESTAMP)  │ │ data_processamento  (TIMESTAMP)│
                                                                         └─────────────────────────────────┘ └────────────────────────────────┘
                                               

```


## Links
- [Dashboards (Looker Studio)](https://lookerstudio.google.com/reporting/14cbaf46-3b91-4c95-9818-e71ce15b1d7a).
- [Repositório](https://github.com/clazinski/case_gb).
