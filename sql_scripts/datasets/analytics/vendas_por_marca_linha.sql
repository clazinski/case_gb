CREATE OR REPLACE TABLE `elevated-bonito-485002-k9.analytics.vendas_por_marca_linha` AS
SELECT
  id_marca,
  marca,
  id_linha,
  linha,
  SUM(qtd_venda)      AS total_vendas,
  COUNT(*)            AS total_registros,
  CURRENT_TIMESTAMP() AS data_processamento
FROM `elevated-bonito-485002-k9.staging.vendas`
GROUP BY 1, 2, 3, 4
ORDER BY total_vendas DESC;