# dagster-baby-pipeline
Playing around with Dagster Data Orchestration framework

# Setting up local Python environment

Ensure you have `pipenv` installed. 
```
pipenv shell
pipenv install dagster dagit
pipenv install dagster_pandas
```

Running locally:
```
dagster pipeline execute -f pipeline.py -c configs/pipeline_config.yaml
```

## Next Steps

- File an issue with import errors when building a workspace/repo def
- - Figure out how add Pandas type hinting
- Understand more about different configs
- Create simple testing with pytest
- Add S3 compatibility for IO using Resource pattern of Dagster
- Add a Jupyter Notebook


# Deploying to EC2 cluster