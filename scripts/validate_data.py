
import pandas as pd
from pathlib import Path

# Dataset location in the GitHub repository
DATA_PATH = Path("data/tourism.csv")

# Expected columns in the tourism dataset
EXPECTED_COLUMNS = [
    "CustomerID",
    "ProdTaken",
    "Age",
    "TypeofContact",
    "CityTier",
    "DurationOfPitch",
    "Occupation",
    "Gender",
    "NumberOfPersonVisiting",
    "NumberOfFollowups",
    "ProductPitched",
    "PreferredPropertyStar",
    "MaritalStatus",
    "NumberOfTrips",
    "Passport",
    "PitchSatisfactionScore",
    "OwnCar",
    "NumberOfChildrenVisiting",
    "Designation",
    "MonthlyIncome"
]


def validate_data():
    """Validate the dataset and display its summary."""

    print("Starting data validation...")

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    # Check required columns
    missing_columns = [
        col for col in EXPECTED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    # Check for an empty dataset
    if df.empty:
        raise ValueError("Dataset is empty.")

    # Check target values
    if not df["ProdTaken"].isin([0, 1]).all():
        raise ValueError(
            "ProdTaken must contain only 0 or 1."
        )

    print("Data validation successful!")
    print("Dataset shape:", df.shape)
    print("Duplicate customers:",
          df["CustomerID"].duplicated().sum())
    print("Missing values:")
    print(df[EXPECTED_COLUMNS].isnull().sum())
    print("Target distribution:")
    print(df["ProdTaken"].value_counts())


if __name__ == "__main__":
    validate_data()
