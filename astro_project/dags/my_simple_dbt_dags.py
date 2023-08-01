"""
### Run a dbt Core project as a task group with Cosmos

Simple DAG showing how to run a dbt project as a task group, using
an Airflow connection and injecting a variable into the dbt project.
"""
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator
from airflow.decorators import dag
from airflow.utils.task_group import TaskGroup
from cosmos.providers.dbt.task_group import DbtTaskGroup
from pendulum import datetime

CONNECTION_ID = "db_conn"
DB_NAME = "mock_project"
SCHEMA_NAME = "public"
DBT_PROJECT_NAME = "dbt_astro"
# the path where Cosmos will find the dbt executable
# in the virtual environment created in the Dockerfile
DBT_EXECUTABLE_PATH = "/usr/local/airflow/dbt_venv/bin/dbt"
# The path to your dbt root directory
DBT_ROOT_PATH = "/usr/local/airflow/dags/dbt"


@dag(
    start_date=datetime(2023, 6, 1),
    schedule=None,
    catchup=False,
)
def my_simple_dbt_dag():

    with TaskGroup(group_id='load_s3_data') as tg_load_data:
        copy_into_revenue_table = S3ToSnowflakeOperator(
            task_id="rev_table",
            snowflake_conn_id="db_conn",
            s3_keys=["rev1.csv"],
            table="rev1",
            stage="my_s3_stage",
            file_format="(TYPE = csv,FIELD_DELIMITER = ',',SKIP_HEADER = 1, empty_field_as_null = TRUE ,null_if = ('NULL', 'null'), FIELD_OPTIONALLY_ENCLOSED_BY='\"')"
        )

        copy_into_crm_table = S3ToSnowflakeOperator(
            task_id="crm_table",
            snowflake_conn_id="db_conn",
            s3_keys=["crm1.csv"],
            table="crm1",
            stage="my_s3_stage",
            file_format="(TYPE = csv,FIELD_DELIMITER = ',',SKIP_HEADER = 1, empty_field_as_null = TRUE ,null_if = ('NULL', 'null'), FIELD_OPTIONALLY_ENCLOSED_BY='\"')"
        )

        copy_into_devices_table = S3ToSnowflakeOperator(
            task_id="device_table",
            snowflake_conn_id="db_conn",
            s3_keys=["device1.csv"],
            table="device1",
            stage="my_s3_stage",
            file_format="(TYPE = csv,FIELD_DELIMITER = ',',SKIP_HEADER = 1, empty_field_as_null = TRUE ,null_if = ('NULL', 'null'), FIELD_OPTIONALLY_ENCLOSED_BY='\"')"
        )
    task = DbtTaskGroup(
        group_id="transform_data",
        dbt_project_name=DBT_PROJECT_NAME,
        conn_id=CONNECTION_ID,
        dbt_root_path=DBT_ROOT_PATH,
        dbt_args={
            "dbt_executable_path": DBT_EXECUTABLE_PATH,
        },
    )
    tg_load_data >> task
my_simple_dbt_dag()

