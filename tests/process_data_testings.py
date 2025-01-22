import pytest
import pandas as pd
import numpy as np

from data_proc import process_data


def test_process_data_series():
    series = pd.Series([1, 2, 3], index=["a", "b", "c"])
    result = process_data(series)
    pd.testing.assert_index_equal(
        result["x"], series.index
    )  # Use pd.testing.assert_index_equal
    assert (
        list(result["y"]) == series.to_list()
    )  # Convert result["y"] to a list for comparison


def test_process_data_dataframe_single_column():
    df = pd.DataFrame({"col1": [1, 2, 3]})
    result = process_data(df)
    pd.testing.assert_series_equal(result["y"], df["col1"])
    assert list(result["x"]) == list(df.index)


def test_process_data_dataframe_two_columns():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    result = process_data(df, x_axis="col1", y_axis="col2")
    pd.testing.assert_series_equal(result["x"], df["col1"])
    pd.testing.assert_series_equal(result["y"], df["col2"])


def test_process_data_dataframe_two_columns_implicit_axes():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    # Suppose to get Value Error here
    with pytest.raises(ValueError) as excinfo:
        process_data(df)  # Implicit x_axis and y_axis
    assert "not found or None." in str(excinfo.value)


def test_process_data_dataframe_multi_columns_with_date():
    df = pd.DataFrame({"Date": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
    result = process_data(df, y_axis="col2")
    pd.testing.assert_series_equal(result["x"], df["Date"])
    pd.testing.assert_series_equal(result["y"], df["col2"])


def test_process_data_dataframe_multi_columns_no_date():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]})
    with pytest.raises(ValueError) as excinfo:
        process_data(df, x_axis="col1")
    assert "not found or None." in str(excinfo.value)


def test_process_data_dataframe_missing_columns():
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    with pytest.raises(ValueError) as excinfo:
        process_data(df, x_axis="col3")
    assert "not found or None." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        process_data(df, x_axis="col1", y_axis="col3")
    assert "not found or None." in str(excinfo.value)


def test_process_data_ndarray_2d():
    array_2d = np.array([[1, 2], [3, 4], [5, 6]])
    result = process_data(array_2d, x_axis=0, y_axis=1)
    expected_x = list(array_2d[:, 0])  # Convert to list
    expected_y = list(array_2d[:, 1])  # Convert to list
    assert list(result["x"]) == expected_x
    assert list(result["y"]) == expected_y


def test_process_data_ndarray_2d_implicit_axes():
    array_2d = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError) as excinfo:
        process_data(array_2d)
    assert "not found or None." in str(excinfo.value)


def test_process_data_ndarray_1d():
    array_1d = np.array([1, 2, 3])
    result = process_data(array_1d)
    assert list(result["x"]) == list(range(len(array_1d)))
    assert list(result["y"]) == list(array_1d)


def test_process_data_list_2d():
    list_2d = [[1, 2], [3, 4], [5, 6]]
    array_2d = np.array(list_2d)
    result = process_data(list_2d, x_axis=0, y_axis=1)
    expected_x = list(array_2d[:, 0])  # Convert to list
    expected_y = list(array_2d[:, 1])  # Convert to list
    assert list(result["x"]) == expected_x
    assert list(result["y"]) == expected_y


def test_process_data_list_2d_implict_axes():
    list_2d = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(ValueError) as excinfo:
        process_data(list_2d)
    assert "not found or None." in str(excinfo.value)


def test_process_data_list_1d():
    list_1d = [1, 2, 3]
    result = process_data(list_1d)
    assert list(result["x"]) == list(range(len(list_1d)))
    assert list(result["y"]) == list_1d


def test_process_data_unsupported_type():
    with pytest.raises(TypeError) as excinfo:
        process_data({"a": 1, "b": 2})  # Dictionary - unsupported type
    assert "Unsupported series type" in str(excinfo.value)


def test_process_data_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as excinfo:
        process_data(df, y_axis="col1")  # Empty DataFrame, y_axis specified
    assert "y_axis column 'col1' not found" in str(excinfo.value)


def test_process_data_reference_name():
    series = pd.Series([1, 2, 3])
    result = process_data(series, reference_name="My Series")
    assert result == {"x": series.index, "y": series.values}


def test_process_data_2d_array_index_error():
    array_2d = np.array([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError) as excinfo:
        process_data(array_2d, x_axis=2)
    assert "not found" in str(excinfo.value)


def test_process_data_2d_list_index_error():
    list_2d = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(ValueError) as excinfo:
        process_data(list_2d, x_axis=2)
    assert "not found" in str(excinfo.value)
