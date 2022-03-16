from flask import Flask, request, render_template, redirect, url_for, jsonify, flash
from PIL import Image
import numpy as np
import torch,logging,os
from utils import Net

app = Flask(__name__)

model = Net()
model.load_state_dict(torch.load('model.pt'))
model.eval()

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir="applicationLogs"
general_logs = "logs"
general_log_path_dir=os.path.join(log_dir,general_logs)

os.makedirs(general_log_path_dir, exist_ok=True)
general_logs_name = "general_logs.log"
general_log_path = os.path.join(general_log_path_dir,general_logs_name)
print(general_log_path)
logging.basicConfig(filename = general_log_path, level=logging.INFO, format=logging_str)
logging.info("Application started")


@app.route('/' , methods = ['GET', 'POST'])
def home():
    logging.info("Home page")
    if request.method == 'POST' and 'image' in request.files:
        try:
            logging.info("POST request")
            img = Image.open(request.files['image'])
            logging.info("Image opened")
            img = img.resize((30,30))
            logging.info("Image resized")

        except Exception as e:
            logging.error("Error in opening image")
            error = 'Could not parse the file as Image media, Try again!!'
            logging.error(error)

            return error

        img = np.expand_dims(np.array(img), axis=0)
        logging.info("Image converted to numpy array")
        img = torch.from_numpy(np.transpose(img, (0, 3, 1, 2))).float()
        logging.info("Image converted to torch tensor")
        _, idx = torch.max(model(img), axis=1)
        logging.info("Prediction done")
        
        prediction = idx.item()
        logging.info(f"Prediction : {prediction}")
        context = {
            'label': idx.item()
        }
        logging.info("Returning context")   
        return jsonify(context)

    else:
        logging.info("GET request")
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)