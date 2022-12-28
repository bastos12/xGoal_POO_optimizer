import os
from model.model import ModelOptimizer
from model.process import (
    DataEncoder,
    DataSplitter,
    EventProcessor
)

if __name__ == "__main__":
    events_file = os.getcwd() + "/data/events.csv"
    info_file = os.getcwd() + "/data/ginf.csv"
    processor = EventProcessor(events_file, info_file)
    processor.process()
    encodeur = DataEncoder(processor.shots)
    encodeur.encode_categorical_variables()
    splitter = DataSplitter(
        data=encodeur.encoded_data.iloc[:,:-1],
        target=encodeur.encoded_data.iloc[:,-1]
    )
    splitter.split()
    optimizer = ModelOptimizer(
        X_train=splitter.X_train,
        X_test=splitter.X_test,
        y_train=splitter.y_train,
        y_test=splitter.y_test
    )
    optimizer.fmin(max_evals=10)
    best_score = optimizer.get_best_score()
    optimized_model = optimizer.choice_best_params(best_score)
    optimizer.evaluate_metrics(optimized_model)