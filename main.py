import pandas as pd
import chardet

import os


def get_csv_file_size(file_path):
    try:
        # Get the size of the file in bytes
        file_size_bytes = os.path.getsize(file_path)

        # Convert bytes to kilobytes or megabytes if needed
        file_size_kb = file_size_bytes / 1024  # Convert bytes to kilobytes
        file_size_mb = file_size_kb / 1024     # Convert kilobytes to megabytes

        return file_size_bytes, file_size_kb, file_size_mb

    except Exception as e:
        print(f"Error getting file size: {e}")
        return None


def get_file_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            # Read a chunk of the file to detect the encoding
            rawdata = f.read()
            result = chardet.detect(rawdata)
            return result['encoding']
    except Exception as e:
        print(f"Error detecting file encoding: {e}")
        return None


def get_csv_metadata(file_path):
    try:
        df = pd.read_csv(file_path)
        column_names = df.columns.tolist()

        data_types = df.dtypes.tolist()

        # summary_statistics = df.describe()

        num_rows, num_columns = df.shape
        metadata = { 
            'column_names': column_names,
            'data_types': data_types,
            # 'summary_statistics': summary_statistics,
            'encoding': get_file_encoding(file_path),
            'num_rows': num_rows,
            'num_columns': num_columns

        }
        return metadata
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


csv_file_path = "data.csv"
metadata = get_csv_metadata(csv_file_path)
if metadata:
    print("CSV file is valid. Metadata:")
    print(metadata)
else:
    print("CSV file is corrupted or cannot be read.")
