from DMHNet.cross_validation import *
from DMHNet.args import create_parser
from DMHNet.utils import *

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    # Checking the rationality of parameters
    if args.dataset == 'DEAP':
        if args.num_class != 2:
            raise ValueError("The parameter num_class is not set correctly.")
        if args.subjects != 32:
            raise ValueError("The parameter subjects is not set correctly.")
        if args.label_type == 'None':
            raise ValueError("The parameter label_type is not set correctly.")
        if args.experiment != 'Dedx':
            raise ValueError("The parameter label_type is not set correctly.")

    elif args.dataset == 'SEED':
        if args.num_class != 3:
            raise ValueError("The parameter num_class is not set correctly.")
        if args.subjects != 15:
            raise ValueError("The parameter subjects is not set correctly.")
        if args.label_type != 'None':
            raise ValueError("The parameter label_type is not set correctly.")



    sub_to_run = np.arange(args.subjects)  # [0, 1, 2, 3, ..., 31]  Train 32 subjects
    # sub_to_run = np.array([0])   # Training of certain subjects


    if args.experiment == 'Dedx':
        cv = CrossValidation(args)
        seed_all(args.random_seed)
        # sub_to_run: [0, 1, 2, 3, ..., 31]   args.reproduce=False
        cv.dependent(subject=sub_to_run, fold=5, reproduce=args.reproduce)  # To do leave one trial out please set fold=40
    elif args.experiment == 'Idex':
        cv = CrossValidation(args)
        seed_all(args.random_seed)
        cv.independence(subject=sub_to_run, fold=10, reproduce=args.reproduce)  # args.reproduce=False
