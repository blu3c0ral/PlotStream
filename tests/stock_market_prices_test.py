import pandas as pd

from PlotStream import run_streamlit_app, register_function


@register_function()
def get_stock_prices():
    df = pd.read_csv("price_data.csv")["closeadj"]
    # make sure the date column is in datetime format
    # df["date"] = pd.to_datetime(df["date"])
    return df


@register_function()
def get_stock_prices_2():

    df = pd.read_csv("price_data_2.csv")[["date", "closeadj"]]

    # make sure the date column is in datetime format
    df["date"] = pd.to_datetime(df["date"])

    return df


print(get_stock_prices())
print(get_stock_prices_2())

run_streamlit_app()  # Defined in PlotStream/__init__.py
