import pandas as pd
import numpy as np

def create_time_features(data):
    data['year'] = data['Date'].dt.year
    data['month'] = data['Date'].dt.month
    data['day'] = data['Date'].dt.day
    data['dayofyear'] = data['Date'].dt.dayofyear
    data['total_days'] = pd.to_datetime(data['Date'].dt.year.astype(str) + '-12-31').dt.dayofyear
    data['cyclic_month'] = np.cos(2 * 3.14 * data['dayofyear'] / data['total_days']) / 2 + 0.5
    data['cyclic_month'] = data['cyclic_month'].round(decimals=2)
    data = data.drop(columns=['dayofyear', 'total_days'])
    return data

if __name__ == "__main__":
    base_dir = "/opt/ml/processing"

    data = pd.read_csv(
        f"{base_dir}/input/min_temperature.csv",
        parse_dates=['Date']
    )
    
    data = create_time_features(data)

    data[data['Date']<'1990-12-01'].to_csv(f"{base_dir}/train.csv", index=False)
    data[data['Date']>='1990-12-01'].to_csv(f"{base_dir}/test.csv", index=False)
