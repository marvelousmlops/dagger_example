from pandas import DataFrame

from topn.preprocess.preprocessor import DataPreprocessor


# Unit tests for DataPreprocessor class
def test_clean_data(mock_raw_data):
    preprocessor = DataPreprocessor(mock_raw_data)
    preprocessor.clean_data()
    output = preprocessor.get_data()

    expected = DataFrame(
        {
            "userId": [
                1,
                1,
                2,
                2,
                3,
            ],
            "movieId": [101.0, 102.0, 101.0, 103.0, 102.0],
            "rating": [5.0, 4.0, 3.0, 2.0, 1.0],
        }
    )

    assert output.shape == (5, 3)
    assert output.equals(expected)


def test_transform_data(mock_raw_data):
    preprocessor = DataPreprocessor(mock_raw_data)
    preprocessor.transform_data()
    output = preprocessor.get_data()

    assert output["userId"].dtype == "int8"
    assert output["movieId"].dtype == "int8"


def test_clean_data_2(sample_raw_data):
    preprocessor = DataPreprocessor(sample_raw_data)
    preprocessor.clean_data()
    assert sample_raw_data.shape == (20, 4)


def test_transform_data_2(sample_raw_data):
    preprocessor = DataPreprocessor(sample_raw_data)
    preprocessor.transform_data()
    assert sample_raw_data["userId"].dtype == "int8"
    assert sample_raw_data["movieId"].dtype == "int8"
