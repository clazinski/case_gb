# Case GB
## Arquitetura proposta
![Arquitetura proposta para o case.](https://i.postimg.cc/1m9vJRkV/arq.png)

## Modelagem
```
                   ┌─────────────────────────────┐
                   │        staging.vendas       │
                   │-----------------------------│
                   │ data_venda                  │
                   │ id_marca / marca            │
                   │ id_linha / linha            │
                   │ qtd_venda                   │
                   └─────────────┬───────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
┌───────────────────┐  ┌───────────────────────┐ ┌───────────────────────┐
│ vendas_por_mes_ano│  │ vendas_por_marca_linha│ │ vendas_por_marca_data │
│-------------------│  │-----------------------│ │-----------------------│
│ ano               │  │ marca                 │ │ marca                 │
│ mes               │  │ linha                 │ │ data_venda            │
│ total_vendas      │  │ total_vendas          │ │ ano / mes             │
│                   │  │                       │ │ total_vendas          │
└───────────────────┘  └───────────────────────┘ └───────────────────────┘
                                                   │
                                         ┌─────────┴────────────┐
                                         │ vendas_por_linha_data│
                                         │----------------------│
                                         │ linha                │
                                         │ data_venda           │
                                         │ ano / mes            │
                                         │ total_vendas         │
                                         └──────────────────────┘
```


## Links
- [Dashboards (Looker Studio)](https://lookerstudio.google.com/reporting/14cbaf46-3b91-4c95-9818-e71ce15b1d7a).
- [Repositório](https://github.com/clazinski/case_gb).
