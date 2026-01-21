import pandas as pd
from google.cloud import storage, bigquery
import io

def load_raw_sales_to_bq(request):
    project_id = "elevated-bonito-485002-k9"
    bucket_name = "case_gb_26"
    files = [
        "Base 2017 (3).xlsx",
        "Base_2018 (3).xlsx",
        "Base_2019 (5).xlsx"
    ]
    table_id = f"{project_id}.raw.vendas"

    storage_client = storage.Client()
    bq_client = bigquery.Client()

    dfs = []

    for file_name in files:
        blob = storage_client.bucket(bucket_name).blob(file_name)
        file_bytes = blob.download_as_bytes()
        df = pd.read_excel(io.BytesIO(file_bytes))
        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)

    df_final.columns = [c.lower() for c in df_final.columns]
    df_final["data_venda"] = pd.to_datetime(df_final["data_venda"], errors="coerce")

    job = bq_client.load_table_from_dataframe(
        df_final,
        table_id,
        job_config=bigquery.LoadJobConfig(
            write_disposition="WRITE_APPEND"
        )
    )

    job.result()
    return "Carga finalizada com sucesso", 200