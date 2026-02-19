CREATE OR REPLACE TABLE `elevated-bonito-485002-k9.staging.vendas` AS
SELECT
  id_marca,
  id_linha,
  CAST(data_venda AS DATE)                     AS data_venda,
  EXTRACT(YEAR FROM CAST(data_venda AS DATE))  AS ano_venda,
  EXTRACT(MONTH FROM CAST(data_venda AS DATE)) AS mes_venda,
  LOWER(TRIM(marca))                           AS marca,
  LOWER(TRIM(linha))                           AS linha,
  CAST(qtd_venda AS INTEGER)                   AS qtd_venda,
  CURRENT_TIMESTAMP()                          AS data_processamento
FROM `elevated-bonito-485002-k9.raw.vendas`;