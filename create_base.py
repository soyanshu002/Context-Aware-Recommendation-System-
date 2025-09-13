import os

# Base = your current project folder
base = os.getcwd()   # get current working directory
print(f"Creating inside: {base}")

# Define the folder structure (without the project folder prefix)
folders = [
    "data/raw",
    "data/processed",
    "data/external",
    "notebooks",
    "src",
    "src/data_preprocessing",
    "src/models",
    "src/recommender_engine",
    "src/utils",
    "tests",
    "reports",
    "reports/figures"
]

# Create empty Python files and notebooks
files = [
    "src/__init__.py",
    "src/data_preprocessing/__init__.py",
    "src/data_preprocessing/load_data.py",
    "src/data_preprocessing/clean_data.py",
    "src/data_preprocessing/feature_engineering.py",
    "src/models/__init__.py",
    "src/models/base_model.py",
    "src/models/collaborative_filtering.py",
    "src/models/context_aware_model.py",
    "src/models/evaluation.py",
    "src/recommender_engine/__init__.py",
    "src/recommender_engine/recommend.py",
    "src/recommender_engine/real_time_api.py",
    "src/recommender_engine/simulation.py",
    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/config.py",
    "src/utils/helpers.py",
    "tests/test_data_preprocessing.py",
    "tests/test_models.py",
    "tests/test_recommender.py",
    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_feature_engineering.ipynb",
    "notebooks/03_model_training.ipynb",
    "requirements.txt",
    "setup.py",
    "README.md",
    "run_pipeline.py",
    "reports/performance_report.xlsx"
]

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base, folder), exist_ok=True)

# Create files (without overwriting existing files)
for file in files:
    path = os.path.join(base, file)
    if not os.path.exists(path):
        with open(path, "w") as f:
            pass

print("Folder structure created successfully!")
