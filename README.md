# Roadmap

* [x] Generate mutated sequences.
* [x] Generate homology models.
* [X] Extract features.
  * [x] MOE: name chains
  * [x] BIOIL: convert to PDB
  * [x] Prepare data.csv (id, pdb_chain, regression value)
  * [x] 3D feature workflow
  * [x] Just select loops
* [x] Model Feed forward NNet.
  * [ ] Script to train it on server.
* [x] Train/test/validate
  * [x] Use Tm2 instead of Tm1
* [X] Find Convolution.
* [x] Model GCNN.
  * [ ] Use message passing
* [x] Train/test/validate.
  * [x] Use Tm2 instead of Tm1

There are two proteins that were introduced in the sequence dataset (AF96737, AF96738).
 - AF96737 HC (A33T, N54Q) LC(G50W)
 - AF96738 GM037v2_VL_G50W,S94T; VH_A33T

The `generate.py` script was modified to account for non-TER-minated chains.

# Selected loops
The Deep Learning models use only loop structures and neighbors of them.

### Light chain
- 26-32
- 49-57
- 91-96

### Heavy chain
- 26-34
- 50-66
- 93-102

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
