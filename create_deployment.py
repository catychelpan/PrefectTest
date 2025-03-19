from prefect import flow

# URL of your GitHub repository
SOURCE_REPO = "https://github.com/catychelpan/PrefectTest.git"

# Import the flow from test_script
from test_script import etl_github_data

# Deploy the flow
if __name__ == "__main__":
    etl_github_data.deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool",  # Specify the work pool name
        cron="0 * * * *",  # Schedule to run every hour
        env={"PREFECT_EXTRAS_REQUIREMENTS": "pandas httpx"},  # Install necessary dependencies
    )
