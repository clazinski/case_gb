CREATE OR REPLACE TABLE `elevated-bonito-485002-k9.staging.vendas` AS
SELECT
  id_marca,
  id_linha,
  SAFE_CAST(data_venda AS DATE)                     AS data_venda,
  EXTRACT(YEAR FROM SAFE_CAST(data_venda AS DATE))  AS ano_venda,
  EXTRACT(MONTH FROM SAFE_CAST(data_venda AS DATE)) AS mes_venda,
  LOWER(TRIM(marca))                                AS marca,
  LOWER(TRIM(linha))                                AS linha,
  SAFE_CAST(qtd_venda AS INT64)                     AS qtd_venda,
  CURRENT_TIMESTAMP()                               AS data_processamento
FROM `elevated-bonito-485002-k9.raw.vendas`;