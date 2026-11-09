import pickle
from flask import Flask, jsonify, request

# Pakia modeli
model_file = 'model.bin'
with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('california-housing')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    
    # Chukua thamani (values) zote kwa mpangilio sahihi unaosubiriwa na modeli
    features = [
        client['longitude'],
        client['latitude'],
        client['housing_median_age'],
        client['total_rooms'],
        client['total_bedrooms'],
        client['population'],
        client['median_income']
    ]
    
    # Fanya utabiri kwa kutumia list ya namba
    prediction = model.predict([features])[0]

    result = {
        'california_housing_prediction': float(prediction)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)