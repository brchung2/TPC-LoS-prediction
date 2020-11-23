from eICU_preprocessing.split_train_test import create_folder
from models.run_lstm import BaselineLSTM
from models.initialise_arguments import initialise_lstm_arguments


if __name__=='__main__':

    c = initialise_lstm_arguments()
    c['mode'] = 'test'
    c['exp_name'] = 'ChannelwiseLSTM'
    c['channelwise'] = True
    c['hidden_size'] = 6
    c['n_epochs'] = 30
    c['dataset'] = 'MIMIC'
    c['no_diag'] = True

    log_folder_path = create_folder('models/experiments/final/MIMIC', c.exp_name)
    channelwise_lstm = BaselineLSTM(config=c,
                                    n_epochs=c.n_epochs,
                                    name=c.exp_name,
                                    base_dir=log_folder_path,
                                    explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    channelwise_lstm.run()