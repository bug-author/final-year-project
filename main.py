import torch.nn as nn
import torch.nn.functional as F


class MnistModel(nn):
    def __init__(self):
        super().__init__()
        self.Linear = nn.Linear(input_size, output_size)

    def forward(self, training_batch):
        # -1 will dynamically set the other dimension
        # for example 
        # input batch => 128, 1, 28, 28
        # reshape => (-1, 28*28) => (-1, 784)
        training_batch = training_batch.reshape(-1, 784)
        output = self.Linear(training_batch)
        return output
    
    def training_step(self, batch):
        images, labels = batch
        output = self(images) # !
        loss = F.cross_entropy(output, labels)
        return loss
