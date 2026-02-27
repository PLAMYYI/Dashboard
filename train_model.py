from autogluon.tabular import TabularPredictor
import pandas as pd

df = pd.read_csv("data.csv")

label = "churn"

predictor = TabularPredictor.load("models/")

predictor.save("models/")

leaderboard = predictor.leaderboard(silent=True)
leaderboard.to_csv("leaderboard.csv", index=False)

importance = predictor.feature_importance(df)
importance.to_csv("feature_importance.csv")