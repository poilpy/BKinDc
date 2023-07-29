import time
import warnings

import torch
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim
import torch.utils.data

from config.config_reader import parse_args, create_parser

from dataloader.load_dataloader import load_dataloader

from model.unsupervised_model_multi_agents import Model
# from model.tusk import Model

from loss.compute_loss import *

from utils import Logger, mkdir_p, save_images
from utils.model_utils import *



def main():

    save_images(tr_inputs, output, epoch, args, epoch, i)




if __name__ == '__main__':
    main()
