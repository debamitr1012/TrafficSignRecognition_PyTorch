from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
from PIL import Image
import numpy as np
import torch
from utils import Net

app = Flask(__name__)

model = Net()
model.load_state_dict(torch.load('model.pt'))
model.eval()

@app.route('/' , methods = ['GET', 'POST'])
def home():
    if request.method == 'POST' and 'image' in request.files:
        try:
            img = Image.open(request.files['image'])
            img = img.resize((30,30))
        except Exception as e:
            error = 'Could not parse the file as Image media, Try again!!'
            return error

        img = np.expand_dims(np.array(img), axis=0)
        img = torch.from_numpy(np.transpose(img, (0, 3, 1, 2))).float()
        _, idx = torch.max(model(img), axis=1)
        prediction = idx.item()
        context = {
            'label': idx.item()
        }
        return jsonify(context)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)