# dagster-baby-pipeline
Playing around with Dagster Data Orchestration framework

## Functionality

## Setting up local Python environment

Ensure you have `pipenv` installed. 
```
pipenv shell
pipenv install dagster dagit dagster_pandas
pipenv install pandas
```

Running locally:
```
dagster pipeline execute -f baby_pipeline.py -d .. --preset local
```

## Next Steps

- ~~File an issue with import errors when building a workspace/repo def~~
- ~~Figure out how add Pandas type hinting~~
- ~~Understand more about different configs~~
- Add S3 compatibility for IO using Resource pattern of Dagster
- Add a Jupyter Notebook
- Testing Strategies
- Schema data validation using Dagster Pandas
- Add Slack messaging

# Cloud Deployment

### Credits

Thanks to my dear friend Vinny with Python wizardry.