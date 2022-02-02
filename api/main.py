from fastapi import FastAPI
import os
import pandas as pd

WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(WORKING_DIR, 'api/data')

app = FastAPI()

@app.get('/')
def home():
    return {
        'Title': 'Artificial Intelligence Empowered Fog Computing',
        'Code': 'https://www.github.com/shy-tan/final-year-project',
        'Authors': ['FA18-BEE-127', 'FA18-BEE-009', 'FA18-BEE-021'],
        }


@app.get('/train-data')
def train_data():
    pos_train_df = pd.read_csv(f'{CACHE}/positions_train_out.csv')

    speeds_train_df = pd.read_csv(f'{CACHE}/speeds_train_out.csv')

    return {
        'speeds_train': speeds_train_df.to_dict(),
        'positions_train': pos_train_df.to_dict(),
    }

@app.get('/test-data')
def test_data():
    pos_test_df = pd.read_csv(f'{CACHE}/positions_test_out.csv')
    speeds_test_df = pd.read_csv(f'{CACHE}/speeds_test_out.csv')

    return {
        'speeds_test': speeds_test_df.to_dict() ,
        'positions_test': pos_test_df.to_dict()
    }