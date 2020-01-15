import torch
import torch.nn as nn


class AADLayer(nn.Module):
    def __init__(self):
        super(AADLayer, self).__init__()

    def forward(self, h_in, zid, zattr):
        # h_in cxnxn
        # zid 256x1x1
        # zattr cxnxn
        pass
