import pandas as pd
from src.features.build_features import create_time_features

def test_time_features_created():
    df = pd.DataFrame(
        {"value": [1, 2]},
        index=pd.to_datetime(["2020-01-01", "2020-01-02"])
    )
    df_feat = create_time_features(df)

    assert "hour" in df_feat.columns
    assert "dayofweek" in df_feat.columns
    assert "month" in df_feat.columns