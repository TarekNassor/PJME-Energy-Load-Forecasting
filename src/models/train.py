import xgboost as xgb
from src.features.build_features import create_time_features

FEATURES = ["hour", "dayofweek", "quarter", "month", "year", "dayofyear"]
TARGET = "PJME_MW"

def train_model(train_df, test_df):
    train_df = create_time_features(train_df)
    test_df = create_time_features(test_df)

    X_train, y_train = train_df[FEATURES], train_df[TARGET]
    X_test, y_test = test_df[FEATURES], test_df[TARGET]

    model = xgb.XGBRegressor(
        n_estimators=1000,
        learning_rate=0.01,
        max_depth=3,
        objective="reg:squarederror",
        early_stopping_rounds=50,
    )

    model.fit(
        X_train,
        y_train,
        eval_set=[(X_test, y_test)],
        verbose=False,
    )

    return model, X_test, y_test