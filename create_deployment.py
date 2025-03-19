from prefect import flow
from test_script import etl_github_data  # Import the flow from your script

# URL of your GitHub repository (you can skip this if you're using a local script)
SOURCE_REPO = "https://github.com/catychelpan/PrefectTest.git"

if __name__ == "__main__":
    etl_github_data.deploy(
        name="my-first-deployment",  # Name of the deployment
        work_pool_name="my-work-pool",  # The work pool you created
        cron="0 * * * *",  # Schedule the flow to run every hour
        # Remove 'env' here as it's no longer used
        extra_requirements=["pandas", "httpx"],  # Ensure dependencies are installed in the environment
    )
