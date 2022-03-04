import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 5) 
        self.conv2 = nn.Conv2d(32, 32, 5) 
        self.pool1 = nn.MaxPool2d(2,2)  
        self.dropout1 = nn.Dropout(0.25) 
        self.conv3 = nn.Conv2d(32, 64, 3) 
        self.conv4 = nn.Conv2d(64, 64, 3) 
        self.pool2 = nn.MaxPool2d(2,2) 
        self.dropout2 = nn.Dropout(0.25) 
        self.fc1 = nn.Linear(3*3*64,256)
        self.dropout3 = nn.Dropout(0.5) 
        self.fc2 = nn.Linear(256, 43) 
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool1(x)
        x = self.dropout1(x)
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = self.pool2(x)
        x = self.dropout2(x)
        x = x.view(-1, 3*3*64)
        x = F.relu(self.fc1(x))
        x = self.dropout3(x)
        x = self.fc2(x)
        return x