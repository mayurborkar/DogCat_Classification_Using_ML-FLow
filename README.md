# It is Dog-Cat Classification Using Mlflow
It is Dog-Cat Classification Model that be implemented using Mlflow.

## Step1: Run The Bash File
```
bash init_setup.sh
```

## Step2: Create The Utils Dir inside src for creating some python repeated file
```
mkdir utils
```
```
touch utils/common.py && touch src/data_mgmt.py && touch src/model.py
```

## Step3: To Use src as package we have run the setup.py file
```
pip install -e .
```

## Step4: Create The src/stage_01_get_data.py file 
```
touch src/stage_01_get_data.py
```

## Step5: Create The src/stage_02_base_model_creation.py file 
```
touch src/stage_02_base_model_creation.py
```

## Step6: Create The src/stage_03_prepare_callbacks.py file 
```
touch src/stage_03_prepare_callbacks.py
```

## Step7: Create The src/stage_04_train.py file 
```
touch src/stage_04_train.py
```

## Step8: Create The main.py For Starting Point 
```
touch src/main.py
```

### Step9: Create the MLproject File To Use Mlops & Run It by Below Command
```
mlflow run . --no-conda
```
### Step10: To run any specific entry point in MLproject file
```
mlflow run . -e get_data --no-conda
```

### Step11: To run any specific entry point in MLproject file
```
mlflow run . -e get_data -P config=configs/your_config.yaml --no-conda
```
