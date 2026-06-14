import pandas as pd

from pipeline.transform import transform_orders


def test_transform_orders_should_calculate_daily_gmv():
    df = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "order_date": ["2026-06-10", "2026-06-10", "2026-06-11"],
            "quantity": [2, 1, 3],
            "price": [10.0, 20.0, 5.0],
        }
    )

    result = transform_orders(df)

    assert list(result.columns) == ["order_date", "daily_gmv"]
    assert result[result["order_date"] == "2026-06-10"]["daily_gmv"].iloc[0] == 40.0
    assert result[result["order_date"] == "2026-06-11"]["daily_gmv"].iloc[0] == 15.0