from train_sl import TrainClassifier
from cords.utils.config_utils import load_config_data

#config_file = "configs/SL/config_glister_cifar10.py"
#config_file = "configs/SL/Regression/config_glister_Cadata.py"
#config_file = "configs/SL/Regression/config_craig_Cadata.py"

config_file = "configs/SL/Regression/config_craig_boston.py"
#config_file = "configs/SL/config_glister_boston.py"
#config_file = "configs/SL/config_full_boston.py"

config_data = load_config_data(config_file)
classifier = TrainClassifier(config_data)

classifier.cfg.dss_args.fraction = 0.1
classifier.cfg.dss_args.select_every = 5
classifier.cfg.train_args.device = 'cuda'
classifier.cfg.train_args.print_every = 1
classifier.cfg.is_reg = True


#classifier.configdata.dss_args.type = "Random"
#classifier.configdata.dss_args.type = "Full"
#classifier.configdata.dataset.name = "LawSchool" #"abalone"
classifier.train()
