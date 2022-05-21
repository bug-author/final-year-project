from fastapi import FastAPI
import os
import pandas as pd

# todos
# new end-points

WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(WORKING_DIR, 'data')
# print(f'{DATA_DIR}/positions_train_out.csv')
app = FastAPI()

@app.get('/')
def home():
    return {
        'Title': 'Artificial Intelligence Empowered Fog Computing',
        'Code': 'https://www.github.com/shy-tan/final-year-project',
        'Authors': ['FA18-BEE-127', 'FA18-BEE-009', 'FA18-BEE-021'],
        'Endpoints': {
            '/train-data': 'Preprocessed train data for both speed and position',
            '/test-data': 'Preprocessed test data for both speed and position',
            '/raw-data': 'Source data'
        }
        }


@app.get('/train-data')
def train_data():
    pos_train_df = pd.read_csv(f'{DATA_DIR}/positions_train_out.csv')

    speeds_train_df = pd.read_csv(f'{DATA_DIR}/speeds_train_out.csv')

    return {
        'speeds_train': speeds_train_df.to_dict(),
        'positions_train': pos_train_df.to_dict(),
    }

@app.get('/test-data')
def test_data():
    pos_test_df = pd.read_csv(f'{DATA_DIR}/positions_test_out.csv')
    speeds_test_df = pd.read_csv(f'{DATA_DIR}/speeds_test_out.csv')

    return {
        'speeds_test': speeds_test_df.to_dict() ,
        'positions_test': pos_test_df.to_dict()
    }

@app.get('/raw-data')
def raw_data():
    raw_df = pd.read_csv(f'{DATA_DIR}/sumo.csv')

    return {
        'raw_data' : raw_df.to_dict(),
    }

@app.get('/data')
def raw_data():
    df = pd.read_csv(f'{DATA_DIR}/whole_data_out.csv')

    return {
        'data' : df.to_dict(),
    }
