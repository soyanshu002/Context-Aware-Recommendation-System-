from flask import Flask, request, jsonify
from src.models.context_aware_model import ContextAwareRecommender

app = Flask(__name__)
model = ContextAwareRecommender()  # Load pre-trained model

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data['user_id']
    context = data['context']
    recommendations = model.predict(user_id, context)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
