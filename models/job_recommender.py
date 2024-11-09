import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.data_loader import load_job_data

def create_job_recommender():
    # Load job data
    job_data = load_job_data()
    job_df = pd.DataFrame(job_data)

    # Create TF-IDF matrix
    tfidf = TfidfVectorizer(stop_words='english')
    job_df['required_skills_text'] = job_df['required_skills'].apply(lambda x: ' '.join(x))
    job_tfidf_matrix = tfidf.fit_transform(job_df['required_skills_text'])

    def recommend_jobs(skills):
        # Convert user input to a TF-IDF vector
        user_profile = ' '.join(skills)
        user_tfidf = tfidf.transform([user_profile])

        # Compute job similarity scores
        similarity_scores = cosine_similarity(user_tfidf, job_tfidf_matrix).flatten()
        job_df['similarity_score'] = similarity_scores
        

        # Filter and sort jobs by score
        top_jobs = job_df.sort_values('similarity_score', ascending=False).head(10)

        # Return top recommendations
        return top_jobs[['job_id', 'job_title', 'company_id', 'required_skills', 'experience_required', 'similarity_score','job_description','location']].to_dict(orient='records')

    return recommend_jobs