import pandas as pd

def read_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame()

def update_csv(data_frame, file_path):
    data_frame.to_csv(file_path, index=False)

def append_to_csv(new_data, file_path):
    new_data = {k: [v] for k, v in new_data.items()}
    data_to_append = pd.DataFrame(new_data)
    data_to_append.to_csv(file_path, mode='a', index=False, header=False)