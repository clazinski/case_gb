CREATE OR REPLACE TABLE `elevated-bonito-485002-k9.analytics.vendas_por_marca_data`
PARTITION BY data_venda
AS
SELECT
  id_marca,
  marca,
  DATE(data_venda)                AS data_venda,
  EXTRACT(YEAR FROM data_venda)   AS ano,
  EXTRACT(MONTH FROM data_venda)  AS mes,
  SUM(qtd_venda)                  AS total_vendas,
  COUNT(*)                        AS total_registros,
  CURRENT_TIMESTAMP()             AS data_processamento
FROM `elevated-bonito-485002-k9.staging.vendas`
GROUP BY 1, 2, 3, 4, 5;