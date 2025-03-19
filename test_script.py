import httpx
import pandas as pd
from datetime import datetime
from prefect import flow, task
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

CSV_FILE = "github_repo_stats.csv"

@task
def fetch_stats(github_repo: str) -> dict:
    """Extract: Fetch GitHub repo data."""
    response = httpx.get(f"https://api.github.com/repos/{github_repo}")
    response.raise_for_status()  # Raise error if request fails
    return response.json()

@task
def extract_stars(repo_stats: dict) -> int:
    """Transform: Extract the number of stars."""
    return repo_stats.get("stargazers_count", 0)

@task
def load_to_csv(repo: str, stars: int):
    """Load: Save the extracted data into a CSV file."""
    data = {"repo": repo, "stars": stars, "timestamp": datetime.now().isoformat()}
    df = pd.DataFrame([data])

    try:
        # Append if file exists, otherwise create a new one
        df.to_csv(CSV_FILE, mode="a", index=False, header=not pd.io.common.file_exists(CSV_FILE))
        print(f"Saved data to {CSV_FILE}: {data}")
    except Exception as e:
        print(f"Error saving data: {e}")

@flow
def etl_github_data():
    """Prefect Flow: Run the full ETL process"""
    github_repos = ["PrefectHQ/prefect", "pydantic/pydantic", "huggingface/transformers"]
    
    for repo in github_repos:
        stats = fetch_stats(repo)
        stars = extract_stars(stats)
        load_to_csv(repo, stars)

if __name__ == "__main__":
    etl_github_data()
