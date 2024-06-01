from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to our web!"

@app.route('/api/coordinates', methods=['POST'])
def process_coordinates():
    data = request.json

    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({"error": "missing latitude and longitude information"}), 400
    
    input_coord = (data['latitude'], data['longitude'])


    # return jsonify(closest_locations)

if __name__ == '__main__':
    app.run(debug=True, port=5000)