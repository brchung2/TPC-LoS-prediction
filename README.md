
Repository for DLH Replication Project: 
===============================

**Citation to the original paper:**
Rocheteau, E., Lio`, P. & Hyland, S. Temporal point- wise convolutional networks for length of stay pre- diction in the intensive care unit. In Proceedings of the Conference on Health, Inference, and Learning, 58–68 (2021). https://arxiv.org/abs/2007.09483

**Link to the original paper’s repo (if applicable):**
https://github.com/EmmaRocheteau/TPC-LoS-prediction

**Dependencies:**
Package Dependencies in: requirements.txt

**Data download instruction:**
Need credentialed access to eICU dataset. 

1) To run the sql files, set up eICU database: https://physionet.org/content/eicu-crd/2.0/. 

2) Follow the instructions: https://eicu-crd.mit.edu/tutorials/install_eicu_locally/ to ensure the correct connection configuration. 


**Preprocessing code + command (if applicable):**

Preprocessing code in : eICU_preprocessing/create_all_tables.sql
Commands: 
1) Clone this repository
2) Replace the eICU_path in `paths.json` to a convenient location in your computer, and do the same for `eICU_preprocessing/create_all_tables.sql` using find and replace for 
`'/content/drive/MyDrive/eICU_data/'`. Leave the extra '/' at the end.

3) In your terminal, navigate to the project directory, then type the following commands:

    ```
    psql 'dbname=eicu user=eicu options=--search_path=eicu'
    ```
    
    Inside the psql console:
    
    ```
    \i eICU_preprocessing/create_all_tables.sql
    ```
    
    This step might take a couple of hours.
    
    To quit the psql console:
    
    ```
    \q
    ```
    
5) Then run the pre-processing scripts in your terminal. This may take a couple hours:

    ```
    python3 -m eICU_preprocessing.run_all_preprocessing
    ```
    
**Training and Evaluation code + command (if applicable)**:
Training and Evaluation code for each model in: models folder listed separately for each model eg 

1) Set the working directory to the TPC-LoS-prediction, and run the following:

    ```
    python3 -m models.run_tpc
    ```
    
    Experiment can be customised by using command line arguments e.g.
    
    ```
    python3 -m models.run_tpc --dataset eICU --task LoS --model_type tpc --n_layers 4 --kernel_size 3 --no_temp_kernels 10 --point_size 10 --last_linear_size 20 --diagnosis_size 20 --batch_size 64 --learning_rate 0.001 --main_dropout_rate 0.3 --temp_dropout_rate 0.1 
    ```
    
    Each experiment you run will create a directory within models/experiments. The naming of the directory is based on 
    the date and time that you ran the experiment (to ensure that there are no name clashes). The experiments are saved 
    in the standard trixi format: https://trixi.readthedocs.io/en/latest/_api/trixi.experiment.html.
    
2) The hyperparameter searches can be replicated by running:

    ```
    python3 -m models.hyperparameter_scripts.eICU.tpc
    ```
 
    Trixi provides a useful way to visualise effects of the hyperparameters (after running the following command, navigate to http://localhost:8080 in your browser):
    
    ```
    python3 -m trixi.browser --port 8080 models/experiments/hyperparameters/eICU/TPC
    ```
    
    The final experiments for the paper are found in models/final_experiment_scripts e.g.:
    
    ```
    python3 -m models.final_experiment_scripts.eICU.LoS.tpc
    ```
    

**Pretrained model (if applicable):**

**Table of results (no need to include additional experiments, but main reproducibility result should be included)**



### Length of Stay Prediction

We report on the following metrics: 
- Mean absolute deviation (MAD)
- Mean absolute percentage error (MAPE)
- Mean squared error (MSE)
- Mean squared log error (MSLE)
- Coefficient of determination (R<sup>2</sup>)
- Cohen Kappa Score (Harutyunyan et al. 2019)

For the first four metrics, lower is better. For the last two, higher is better.

#### eICU

Model | MAD | MAPE | MSE | MSLE | R<sup>2</sup> | Kappa
--- | --- | --- | --- | --- | --- | ---
Mean* | 3.21 | 395.7 | 29.5 | 2.87 | 0.00 | 0.00
Median* | 2.76 | 184.4 | 32.6 | 2.15 | -0.11 | 0.00
LSTM | 2.39±0.00 | 118.2±1.1 | 26.9±0.1 | 1.47±0.01 | 0.09±0.00 | 0.28±0.00
CW LSTM | 2.37±0.00 | 114.5±0.4 | 26.6±0.1 | 1.43±0.00 | 0.10±0.00 | 0.30±0.00
Transformer | 2.36±0.00 | 114.1±0.6 | 26.7±0.1 | 1.43±0.00 | 0.09±0.00 | 0.30±0.00
TPC | 1.78±0.02 | 63.5±4.3 | 21.7±0.5 | 0.70±0.03 | 0.27±0.02 | 0.58±0.01

Our model (TPC) significantly outperforms all baselines by large margins. 
*The mean and median "models" always predict 3.47 and 1.67 days respectively (the mean and median of the training set).



#### eICU

Model | AUROC | AUPRC | MAD | MAPE | MSE | MSLE | R<sup>2</sup> | Kappa
--- | --- | --- | --- | --- | --- | --- | --- | ---
LSTM | 0.852±0.003 | 0.436±0.007 | 2.40±0.01 | 116.5±0.8 | 27.2±0.2 | 1.47±0.01 | 0.08±0.01 | 0.28±0.01
CW LSTM | 0.865±0.002 | 0.490±0.007 | 2.37±0.00 | 115.0±0.7 | 26.8±0.1 | 1.44±0.00 | 0.09±0.00 | 0.30±0.00
Transformer | 0.858±0.001 | 0.475±0.004 | 2.36±0.00 | 114.2±0.7 | 26.6±0.1 | 1.43±0.00 | 0.10±0.00 | 0.30±0.00
TPC | 0.865±0.002 | 0.523±0.006 | 1.55±0.01 | 46.4±2.6 | 18.7±0.2 | 0.40±0.02 | 0.37±0.01 | 0.70±0.00



