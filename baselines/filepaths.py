import os
from pathlib import Path

filepaths_path = Path(os.path.dirname(os.path.abspath(__file__)))
home_path = filepaths_path / '..'

HOME_DIR = str(home_path) #FLIP home directory
BASELINE_DIR = str(home_path / 'baselines')
DATA_DIR = str(home_path / 'splits')

EMBEDDING_DIR = 'embeddings/'
RESULTS_DIR = '../FLIP_results/'

SEQ_MODELS = '../sequence_models' #link to sequence_paths submodule

