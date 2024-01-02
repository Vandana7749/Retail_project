import pytest
from lib.utils import get_spark_session
from lib.DataReader import read_customers, read_orders
from lib.DataManipulation import filter_closed_orders, count_orders_state, generic_filter
from lib.configReader import get_app_config

@pytest.mark.skip()
def test_read_customers_df(spark):
    customers_count = read_customers(spark,'LOCAL').count()
    assert customers_count == 12435

@pytest.mark.skip()
def test_read_orders_df(spark):
    orders_count = read_orders(spark,'LOCAL').count()
    assert orders_count == 68884

@pytest.mark.skip()
@pytest.mark.transformation
def test_filter_closed_orders(spark):
    orders_df = read_orders(spark, 'LOCAL')
    filtered_count = filter_closed_orders(orders_df).count()
    assert filtered_count == 7556

@pytest.mark.skip()
def test_get_app_config():
    config = get_app_config('LOCAL')
    assert config['orders.file.path'] == 'data/orders.csv'

# @pytest.mark.transformation
# def test_count_orders_state(spark, expected_results):
#     customers_df = read_orders(spark, "LOCAL")
#     actual_results = count_orders_state(customers_df)
#     assert actual_results.collect() == expected_results.collect()

@pytest.mark.parametrize(
    "status,count",
    [("CLOSED", 7556),
     ("PENDING", 7610),
     ("COMPLETE", 22900)]
)
def test_check_count(spark, status, count):
    orders_df = read_orders(spark, 'LOCAL')
    filtered_count = generic_filter(orders_df, status).count()
    assert filtered_count == count