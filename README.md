# Modele xGoal
____


Le projet est de créer un module de classification xGoal. Les données ont été récupérées sur plus de 250 000 tirs lors de saison 2015.

Il utilise un model de classification *GradientBoostingClassifier* et peut être changer dans le fichier model.py

Veillez a bien decompresser le fichier event.zip present dans le dossier data afin d'obtenir les deux csv events necessaire **event.csv** et **ginf.csv**

#### Structuration du projet

├───data
│   └─────const.py
│   └─────event.csv
│   └─────ginf.csv
└───model
│   └─────model.py
│   └─────process.py
├───classifier.py
├───README.md
├───requirements.txt


#### Scores (K-Top5)

| passage | learning_rate | min_samples_leaf | max_depth | max_features | train_ROCAUC | test_ROCAUC | recall   | precision | f1_score | train_accuracy | test_accuracy | loss      | status |
|---------|---------------|------------------|-----------|--------------|--------------|-------------|----------|-----------|----------|----------------|---------------|-----------|--------|
| 6       | 0.220807      | 139              | 7         | 16           | 0.818083     | 0.819127    | 0.267404 | 0.716672  | 0.389484 | 0.910439       | 0.911108      | -0.819127 | ok     |
| 7       | 0.185222      | 23               | 10        | 11           | 0.819106     | 0.818228    | 0.267992 | 0.709748  | 0.389074 | 0.910566       | 0.910758      | -0.818228 | ok     |
| 9       | 0.196736      | 151              | 14        | 16           | 0.818530     | 0.818736    | 0.266698 | 0.717494  | 0.388856 | 0.910425       | 0.911108      | -0.818736 | ok     |
| 8       | 0.209266      | 103              | 11        | 17           | 0.818678     | 0.818609    | 0.266698 | 0.716135  | 0.388656 | 0.910486       | 0.911033      | -0.818609 | ok     |
| 0       | 0.114414      | 170              | 15        | 23           | 0.818230     | 0.818869    | 0.266345 | 0.717681  | 0.388508 | 0.910304       | 0.911095      | -0.818869 | ok     |

#### Rapport de classification
|              | Precision | Recall | f1-score | support | 
|--------------|-----------|--------|----------|-
| No Goal      | 0.92      | 0.99   | 0.95     | 71694 
| Goal         | 0.72      | 0.27   | 0.39     | 8504 
| Accuracy     |           |        | 0.91 
| Macro avg    | 0.82      | 0.63   | 0.67  
| Weighted avg | 0.90      | 0.91   | 0.89 

#### Projection

Un travail de reequilibrage est necessaire pour obtenir un meilleur recall est donc améliorer le modèle.
Ici, nous avons seulement effectué une optimisation des paramètres du modèle.
Rééquilibrer les classes serait donc une options a effectuer pour améliorer significativement la précision du modele et notamment du recall.

#### Install

Créer son dossier et se placer à l'interieur
```
cd ./[votre_dossier]
```
Installer l'environnement virtuel et les dependances
```
# windows
virtualenv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt 
```
#### Run

```
py classifier.py
```

#### Output
- Impression du travail d'optimisation dans la console
- Impression des bests scores obtenus
- Impression des metrics du modele
___


### Contact

Tu peux visiter mon site pour plus de projets [sportdatalab](https://www.sportdatalab.fr/projects) ou pour me [contacter](https://www.sportdatalab.fr/contact).

### Licence

MIT


