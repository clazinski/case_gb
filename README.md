# Case GB
## Arquitetura proposta
![Arquitetura proposta para o case.](https://i.postimg.cc/1m9vJRkV/arq.png)

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
