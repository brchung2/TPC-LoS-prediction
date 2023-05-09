
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

Preprocessing code in : eICU_preprocessing/create_all_tables.sql.

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

Training and Evaluation code for each model listed separately:
eg models/run_tpc.py to run the TPC model; models/run_lstm.py to run the LSTM model.

1) Set the working directory to the TPC-LoS-prediction, and run the following command:

Specify command line arguments to hyperparameter values:
    
    ```
    
    python3 -m models.run_tpc --dataset eICU --task LoS --model_type tpc --percentage_data 10  #TPC model
    python3 -m models.run_LSTM --dataset eICU --task LoS --model_type lstm --percentage_data 10 #LSTM model
    python3 -m models.run_transformer --dataset eICU --task LoS --model_type transformer --percentage_data 10 #Transformer model  
    
    ```
 2) Run this script to run experiments: 

     ```
    python3 -m models.hyperparameter_scripts.eICU.hyperparameter_tuning_exp 
    ```
   

**Pretrained model (if applicable):**

**Table of results (no need to include additional experiments, but main reproducibility result should be included)**

Presentation slides:
https://docs.google.com/presentation/d/1-GQfAKFpgfdcnkTdKmeyAoaGeWNCnBUxEgQbWf3nc6I/edit#slide=id.g222d1ba3356_0_134

Performance for each model on 10\% data and the improvement range \% of the TPC model over the best baseline. Bolded metric numbers show the best model is TPC for each metric.

![image](https://user-images.githubusercontent.com/88016352/236999387-c3c8e9fa-5a29-4ccd-958c-3389c8acce33.png)


