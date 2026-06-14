from pathlib import Path

from pipeline.transform import load_orders, save_output, transform_orders


ROOT_DIR = Path(__file__).resolve().parents[1]


def main() -> None:
    input_path = ROOT_DIR / "data" / "input" / "orders.csv"
    output_path = ROOT_DIR / "dist" / "daily_gmv.csv"

    orders = load_orders(input_path)
    result = transform_orders(orders)
    save_output(result, output_path)

    print(f"Generated output: {output_path}")


if __name__ == "__main__":
    main()