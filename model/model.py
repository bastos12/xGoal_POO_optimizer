import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    average_precision_score,
    roc_auc_score,
    f1_score,
    precision_score,
    recall_score,
    cohen_kappa_score,
    classification_report,
    confusion_matrix
)
from hyperopt import (
    hp,
    Trials,
    STATUS_OK,
    fmin,
    tpe
)
from data.const import Color


class ModelOptimizer:
    def __init__(self, X_train, y_train, X_test, y_test):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.hyperparameter_space = {
            'learning_rate': hp.uniform('learning_rate', 0.05, 0.3),
            'min_samples_leaf': hp.choice('min_samples_leaf', range(15, 200)),
            'max_depth': hp.choice('max_depth', range(2, 20)),
            'max_features': hp.choice('max_features', range(3, 27))
        }
        self.trials = Trials()
    
    def evaluate_model(self, params):
        model = GradientBoostingClassifier(
                    learning_rate=params['learning_rate'],
                    min_samples_leaf=params['min_samples_leaf'],
                    max_depth = params['max_depth'],
                    max_features = params['max_features']
                    )
        model.fit(self.X_train, self.y_train)
        return {
            'learning_rate': params['learning_rate'],
            'min_samples_leaf': params['min_samples_leaf'],
            'max_depth': params['max_depth'],
            'max_features': params['max_features'],
            'train_ROCAUC': roc_auc_score(self.y_train, model.predict_proba(self.X_train)[:, 1]),
            'test_ROCAUC': roc_auc_score(self.y_test, model.predict_proba(self.X_test)[:, 1]),
            'recall': recall_score(self.y_test, model.predict(self.X_test)),
            'precision': precision_score(self.y_test, model.predict(self.X_test)),
            'f1_score': f1_score(self.y_test, model.predict(self.X_test)),
            'train_accuracy': model.score(self.X_train, self.y_train),
            'test_accuracy': model.score(self.X_test, self.y_test),
        }
    
    def objective(self, params):
        res = self.evaluate_model(params)
        res['loss'] = - res['test_ROCAUC']
        res['status'] = STATUS_OK
        return res 

    def fmin(self, max_evals):
        fmin(
            self.objective,
            space=self.hyperparameter_space,
            algo=tpe.suggest,
            max_evals=max_evals,
            trials=self.trials
            )
    
    def get_best_score(self, metric='f1_score', ascending=False):
        best_score = pd.DataFrame(self.trials.results).sort_values(by=metric, ascending=ascending).head(5)
        print(best_score)
        return best_score
    
    def choice_best_params(self, best_score):
        model = GradientBoostingClassifier(
                        learning_rate=best_score['learning_rate'][0],
                        min_samples_leaf=best_score['min_samples_leaf'][0],
                        max_depth = best_score['max_depth'][0],
                        max_features = best_score['max_features'][0]
                        )
        model.fit(self.X_train, self.y_train)
        return model
    
    def evaluate_metrics(self, model):
        print('Le jeu de test contient {} examples de tir et {} sont des buts.'.format(len(self.y_test), self.y_test.sum()))
        print('Le model obtien une ROC-AUC de {}%'.format(round(roc_auc_score(self.y_test, model.predict_proba(self.X_test)[:, 1])*100),2))
        print('La performance de base pour PR-AUC est de {}%.'.format(round(self.y_train.mean(),2)))
        print('Le modele obtien une PR-AUC de {}%.'.format(round(average_precision_score(self.y_test, model.predict_proba(self.X_test)[:, 1])*100,2)))
        print('Le modele obtien un Cohen Kappa de {}.'.format(round(cohen_kappa_score(self.y_test,model.predict(self.X_test)),2)))
        print(Color.BOLD + Color.YELLOW + 'Matrice de confusion:\n' + Color.END)
        print(confusion_matrix(self.y_test,model.predict(self.X_test)))
        print(Color.BOLD +  Color.YELLOW + '\n Rapport de classification:' + Color.END)
        print(classification_report(self.y_test,model.predict(self.X_test)))
        print('\n Probabilités xGoal:', model.predict_proba(self.X_test))
    
