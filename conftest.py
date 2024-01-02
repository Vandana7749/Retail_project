import pytest
from lib.utils import get_spark_session

@pytest.fixture
def spark():
    "creates spark session"
    spark_session= get_spark_session('LOCAL')
    yield spark_session
    spark_session.stop()

@pytest.fixture
def expected_results(spark):
    "reading the data from data/test_data folder"
    results_schema = "state string, count int"
    return spark.read \
    .format('csv') \
    .schema(results_schema) \
    .load('data/test_data/state_aggregated.csv')
