import os
from bpm_processing import calculate_bpm


def test_bpm_processing():
    dirname = os.path.dirname(__file__)
    data_path = os.path.join(dirname, "data")
    list_of_files = os.listdir(data_path)
    for file in list_of_files:
        file_path = os.path.join(data_path, file)
        print(calculate_bpm(file_path))

test_bpm_processing()