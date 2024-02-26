import pandas as pd
import pytest


# Loading mock data for testing
@pytest.fixture(scope="session")
def mock_data():
    mock_data = pd.DataFrame(
        {
            "userId": [1, 1, 2, 2, 3],
            "movieId": [101, 102, 101, 103, 102],
            "rating": [5, 4, 3, 2, 1],
        }
    )
    return mock_data


# Loading mock data for testing
@pytest.fixture(scope="session")
def sample_data():
    sample_data = pd.read_csv("tests/resources/processed_ratings.csv")
    return sample_data


# Creating mock data for testing
@pytest.fixture(scope="session")
def mock_gold_data():
    gold_data = {
        3: [0, 11, 18, 17, 16],
        11: [7, 1, 18, 17, 16],
        16: [11, 1, 12, 17, 15],
        17: [0, 3, 18, 16, 15],
    }

    return gold_data


# Creating mock data for testing
@pytest.fixture(scope="session")
def mock_raw_data():
    mock_raw_data = pd.DataFrame(
        {
            "userId": [1, 1, 2, 2, 3, 4, 5],
            "movieId": [101, 102, 101, 103, 102, None, 104],
            "rating": [5, 4, 3, 2, 1, 3, None],
        }
    )

    return mock_raw_data


# Loading mock data for testing
@pytest.fixture(scope="session")
def sample_raw_data():
    raw_data = pd.read_csv("tests/resources/ratings.csv")
    return raw_data
