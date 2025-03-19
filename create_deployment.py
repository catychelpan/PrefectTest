from prefect import flow

# URL of your repository
SOURCE_REPO = "https://github.com/catychelpan/PrefectTest.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="your_flow_script.py:your_flow_function",  # Replace with your flow file and function name
    ).deploy(
        name="my-first-deployment",  # Name of the deployment
        parameters={  # Add any parameters that your flow might need
            "example_param": "value"
        },
        work_pool_name="my-work-pool",  # Work pool you created earlier
        cron="0 * * * *",  # Schedule the flow to run every hour
    )
