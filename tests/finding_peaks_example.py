import pandas as pd

from scipy.ndimage import median_filter

from plotstream import run_plotstream_app, plotstream_function


@plotstream_function()
def get_stock_prices():

    df = pd.read_csv("price_data.csv")[["date", "closeadj"]]

    # make sure the date column is in datetime format
    df["date"] = pd.to_datetime(df["date"])

    return df


@plotstream_function()
def median_smooth_stock_prices(windowsize: int = 5):
    df = get_stock_prices()
    df["smoothed"] = median_filter(df["closeadj"], size=windowsize)
    # Remove closeadj column
    df = df.drop("closeadj", axis=1)

    return df


@plotstream_function()
def sma_smooth_stock_prices(windowsize: int = 5):
    df = get_stock_prices()
    df["smoothed"] = df["closeadj"].rolling(window=windowsize).mean()
    # Remove closeadj column
    df = df.drop("closeadj", axis=1)

    return df


run_plotstream_app()
