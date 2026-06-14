from pathlib import Path

import pandas as pd


def load_orders(input_path: str | Path) -> pd.DataFrame:
    return pd.read_csv(input_path)


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["amount"] = df["quantity"] * df["price"]

    result = (
        df.groupby("order_date", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "daily_gmv"})
    )

    return result


def save_output(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)