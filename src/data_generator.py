# Created first backend module that generates employee activity data.

This data will be used by AI to detect insider threats.
import pandas as pd
import numpy as np

def generate_employee_data(num_records=500):

    np.random.seed(42)

    data = {
        "employee_id": np.random.randint(1000, 1100, num_records),
        "login_hour": np.random.randint(0, 24, num_records),
        "files_accessed": np.random.randint(1, 50, num_records),
        "data_downloaded_mb": np.random.randint(10, 500, num_records),
        "usb_usage": np.random.randint(0, 2, num_records)
    }

    df = pd.DataFrame(data)

    return df


if __name__ == "__main__":
    df = generate_employee_data()
    print(df.head())

