import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://crzvbcbpgvxpkdnksbuy.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNyenZiY2JwZ3Z4cGtkbmtzYnV5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA1NzA0NzYsImV4cCI6MjA0NjE0NjQ3Nn0.QJrEtgM1slLBefid98NMw1kLxaBCCMKWpYQ9-5-qZA4")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def load_job_data():
    response = supabase.table('jobs').select("job_id, job_title, company, required_skills, experience_required, job_description, location").execute()
    job_data = response.data
    job_data = [
        {
            "job_id": row["job_id"],
            "job_title": row["job_title"],
            "company_id": row["company_id"],
            "required_skills": row["required_skills"].split(","),
            "experience_required": int(row["experience_required"]),
            "job_description": row["job_description"],
            "location":row["location"]
        }
        for row in job_data
    ]
    return job_data