import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split

from data.const import (
    COLUMNS_ENCODE,
    ENCODED_COLUMNS
)

class EventProcessor:
    def __init__(self, events_file, info_file):
        self.events = pd.read_csv(events_file, sep=",", header=0)
        self.info = pd.read_csv(info_file, sep=",", header=0)
    
    def process(self):
        self.events = self.events.merge(self.info[['id_odsp', 'country', 'date']], on='id_odsp', how='left')
        extract_year = lambda x: datetime.strptime(x, "%Y-%m-%d").year
        self.events['year'] = [extract_year(x) for key, x in enumerate(self.events['date'])]
        self.shots = self.events[self.events.event_type==1]
        self.shots['player'] = self.shots['player'].str.title()
        self.shots['player2'] = self.shots['player2'].str.title()
        self.shots['country'] = self.shots['country'].str.title()

class DataEncoder:
    def __init__(self, data):
        self.data = data
    
    def encode_categorical_variables(self):
        encoded_data = pd.get_dummies(self.data.iloc[:,-8:-3], columns=COLUMNS_ENCODE)
        encoded_data.columns = ENCODED_COLUMNS
        encoded_data['is_goal'] = self.data['is_goal']
        self.encoded_data = encoded_data

class DataSplitter:
    def __init__(self, data, target, test_size=0.35, random_state=1):
        self.data = data
        self.target = target
        self.test_size = test_size
        self.random_state = random_state
    
    def split(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.target, test_size=self.test_size, random_state=self.random_state)
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test