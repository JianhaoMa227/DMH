import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    ######## Data ########
    parser.add_argument('--dataset', type=str, default='DEAP', choices=['DEAP', 'SEED'])

    parser.add_argument('--subjects', type=int, default=32, choices=['15', '32'], help='SEED:15, DEAP:32')
    parser.add_argument('--num_class', type=int, default=2, choices=[2, 3, 4, 5], help='SEED:3, SEED4: num_class=4, SEED5: num_class=5, DEAP: num_class=2')
    parser.add_argument('--label_type', type=str, default='V', choices=['A', 'V', 'None'], help='SEED: label_type=None, DEAP: label_type=V or A')

    parser.add_argument('--data-format', type=str, default='raw')
    ######## Training Process ########
    parser.add_argument('--random-seed', type=int, default=1234)
    parser.add_argument('--max-epoch', type=int, default=500)
    parser.add_argument('--batch-size', type=int, default=512)
    parser.add_argument('--learning-rate', type=float, default=1e-4)
    parser.add_argument('--dropout', type=float, default=0.2)

    parser.add_argument('--save-path', default='./save_mjh/')
    parser.add_argument('--load-path', default='./save_mjh/max-acc.pth')
    parser.add_argument('--gpu', default='0')
    parser.add_argument('--save-model', type=bool, default=True)
    ######## Model Parameters ########
    parser.add_argument('--model', type=str, default='DMH',

                        help='DMH, '
                             'MSM, MSM_HWT, DySample_MSM '
                             'Interpolate_MSM_HWT, TransSample_MSM_HWT, PixelShuffle_MSM_HWT, CARAFE_MSM_HWT,'
                             ''
                             'EEGNet, MLP, RNN, LSTM, CNN, GRU'
                             'DySample_EEGNet, DySample_MLP, DySample_RNN, DySample_LSTM, DySample_CNN, DySample_GRU')

    ######## Reproduce the result using the saved model ######
    parser.add_argument('--reproduce', type=bool, default=False)

    parser.add_argument('--experiment', type=str, choices=['Idex', 'Dedx'], default='Dedx',
                        help='independent dependence experiment')


    return parser