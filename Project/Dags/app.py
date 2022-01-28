try:
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime

    print("Everything works well")

except Exception as e:
    print("Error  {} ".format(e))


def fun():
    print(" For example ")
    return " Example "


with DAG(
        dag_id="app",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=3),
            "start_date": datetime(2022, 10, 10),
        },
        catchup=False
) as f:
    fun = PythonOperator(
        task_id="fun",
        python_callable=fun
    )



