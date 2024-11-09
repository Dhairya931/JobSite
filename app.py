from flask import Flask, request, jsonify
from flask_cors import CORS
from models.job_recommender import create_job_recommender

app = Flask(__name__)
CORS(app)

@app.route('/recommend_jobs', methods=['POST'])
def recommend_jobs():
    skills = request.json['skills']
    # experience = request.json['experience']
    job_recommender = create_job_recommender()
    recommended_jobs = job_recommender(skills)
    if recommended_jobs:
        return jsonify(recommended_jobs)
    else:
        return jsonify([])
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)