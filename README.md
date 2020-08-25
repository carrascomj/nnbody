# Roadmap

* [x] Generate mutated sequences.
* [x] Generate homology models.
* [ ] Extract features.
  * [x] MOE: name chains
  * [x] BIOIL: convert to PDB
  * [x] Prepare data.csv (id, pdb_chain, regression value)
  * [ ] 3D feature workflow
  * [ ] Just select loops
* [ ] Model Feed forward NNet.
* [ ] Train/test/validate
* [ ] Find Convolution.
* [ ] Model GCNN.
* [ ] Train/test/validate.

## Guided tour
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interm        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── process            <- Scripts to download or generate data
    │   │   ├── mutate.py      <- Generate FASTA files for the mutated sequences
    │   │   └── put_chains.py  <- Annotate missing chains of a MOE generated PDB.
    │   │
    │   ├── features              <- Scripts to turn raw data into features for modeling
    │   │   ├── generate.py       <- Script to convert PDBs to features
    │   │   └── protein_graph.py  <- out-of-memory dataloader/data augmentation
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
