# # scipy
# import scipy
# print('scipy: %s' % scipy.__version__)
# print("Hello to Bosh Release")
# # numpy
# import numpy
# print('numpy: %s' % numpy.__version__)
# matplotlib
# import matplotlib
# print('matplotlib: %s' % matplotlib.__version__)
# pandas
# import pandas
# print('pandas: %s' % pandas.__version__)
# # statsmodels
# import statsmodels
# print('statsmodels: %s' % statsmodels.__version__)
# # scikit-learn
# import sklearn
# print('sklearn: %s' % sklearn.__version__)
# import requests
# print('requests: %s' % requests.__version__)
# import h5py
# print('h5py: %s' % h5py.__version__)

# print("Hello to Bosh Release")

#!flask/bin/python
from flask import Flask, jsonify
import numpy, pandas, requests, scipy, sklearn, h5py, flask, tensorflow, keras

app = Flask(__name__)

@app.route('/')
def index():
    versions = {
        'numpy' : numpy.__version__,
        'pandas' : pandas.__version__,
        'requests' : requests.__version__,
        'scipy' : scipy.__version__,
        'scikit-learn' : sklearn.__version__,
        'h5py' : h5py.__version__,
        'flask' : flask.__version__,
        'tensorflow' : tensorflow.__version__,
        'keras' : keras.__version__
    }
    return jsonify({'versions': versions})

if __name__ == '__main__':
    app.run(port=8080, debug=True)