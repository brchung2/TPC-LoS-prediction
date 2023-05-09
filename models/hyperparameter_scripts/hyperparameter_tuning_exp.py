from eICU_preprocessing.split_train_test import create_folder
from models.run_tpc import TPC
import numpy as np
import random
from models.final_experiment_scripts.best_hyperparameters import best_global
from models.initialise_arguments import initialise_tpc_arguments


def get_hyperparam_config(dataset):

    c = initialise_tpc_arguments()
    c['mode'] = 'train'
    c['exp_name'] = 'TPC'
    if dataset == 'MIMIC':
        c['no_diag'] = True
    c['dataset'] = dataset
    c['model_type'] = 'tpc'
    c['percentage_data'] = 10
    c = best_global(c)   
    return c


if __name__=='__main__':
    temp_dropout_rate = [0, 0.025, 0.05, 0.075, 0.1, 0.15, 0.2]
    point_sizes = [3,5,7,10,13]
    main_dropout_rate = [0.1125, 0.225, 0.45]
    batch_size = [4,8,16,32]
    learning_rate = [0.001, 0.00226, 0.003, 0.005]

    list_of_hyperparams = [('temp_dropout_rate',temp_dropout_rate), ('point_sizes',point_sizes), 
    ('main_dropout_rate', main_dropout_rate), ('batch_size', batch_size), ('learning_rate',learning_rate)]
    for param_name, paramlist in list_of_hyperparams:
        for i in paramlist:
            print('param = ', param_name)
            print('value = ', i)
            try:
                c = get_hyperparam_config('eICU')
                c[param_name] = i
                log_folder_path = create_folder('models/experiments/hyperparameters/eICU', c.exp_name)
                tpc = TPC(config=c,
                        n_epochs=c.n_epochs,
                        name=c.exp_name,
                        base_dir=log_folder_path,
                        explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
                tpc.run()

            except RuntimeError:
                continue