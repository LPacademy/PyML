from flask import request
from flask_api import FlaskAPI
import os
import uuid
import vgg16_classifier
from json_encoders import MyEncoder

app = FlaskAPI(__name__)
app.json_encoder = MyEncoder

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        filepath = os.path.join(os.getcwd(), f_name)
        file.save(filepath)
        results = vgg16_classifier.predict(f_name)
        os.remove(filepath)
        return results


if __name__ == "__main__":
    app.run(port=5001, debug=True)
