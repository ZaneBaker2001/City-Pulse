from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

def train_model(df):
    X = df[['temp', 'humidity', 'wind_speed', 'hour', 'dayofweek', 'pm25_rolling']]
    y = df['pm25']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"Model RMSE: {rmse:.2f}")

    joblib.dump(model, "model.pkl")
    return model