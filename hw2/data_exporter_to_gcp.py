from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import pyarrow as pa
import pyarrow.parquet as pq
from os import path
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/dtc-de-course-411401-fbe71733ecc5.json"

bucket_name = 'mage-zoomcamp-dtamrazov'
table_name = 'daily-trips-green-taxi'

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(df: DataFrame, *args, **kwargs) -> None:

    table = pa.Table.from_pandas(df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ["lpep_pickup_date"],
        filesystem = gcs
    )
