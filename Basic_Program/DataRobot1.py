import datarobot as dr

import pandas as pd

pd.options.display.max_columns = 1000

import numpy as np

import time

import matplotlib.pyplot as plt

from jupyterthemes import jtplot

# currently installed theme will be used to set plot style if no arguments provided

jtplot.style()

get_ipython().magic('matplotlib inline')

# load input data
df = pd.read_csv('../demo_data/10kDiabetes.csv')

# initialize datarobot client instance
dr.Client(config_path='/Users/benjamin.miller/.config/datarobot/my_drconfig.yaml')

# create 100 samples with replacement from the original 10K diabetes dataset

samples = []

for i in range(100):
   samples.append(df.sample(10000, replace=True))

# loop through each sample dataframe

for i, s in enumerate(samples):
   # initialize project
   project = dr.Project.start(
       project_name='API_Test_{}'.format(i+20),
       sourcedata=s,
       target='readmitted',
       worker_count=2
   )

# get all projects

projects = []

for project in dr.Project.list():

    if "API_Test" in project.project_name:
        projects.append(project)

# *For each project...*

# Make predictions on the original dataset using the most accurate model


# initialize list of all predictions for consolidating results

bootstrap_predictions = []

# loop through each relevant project to get predictions on original input dataset

for project in projects:

    # get best performing model

    model = dr.Model.get(project=project.id, model_id=project.get_models()[0].id)

    # upload dataset

    new_data = project.upload_dataset(df)

    # start a predict job

    predict_job = model.request_predictions(new_data.id)

    # get job status every 5 seconds and move on once 'inprogress'

    for i in range(100):

        time.sleep(5)

        try:
            job_status = dr.PredictJob.get(
                project_id=project.id,
                predict_job_id=predict_job.id
            ).status
        except:  # normally the job_status would produce an error when it is completed
            break
    # now the predictions are finished
    predictions = dr.PredictJob.get_predictions(
        project_id=project.id,
        predict_job_id=predict_job.id
    )
    # extract row ids and positive probabilities for all records and set to dictionary
    pred_dict = {k: v for k, v in zip(predictions.row_id, predictions.positive_probability)}

    # append prediction dictionary to bootstrap predictions

    bootstrap_predictions.append(pred_dict)

# combine all predictions into single dataframe with keys as ids
# each record is a row, each column is a set of predictions pertaining to

# a model created from a bootstrapped dataset
df_predictions = pd.DataFrame(bootstrap_predictions).T

# add mean predictions for each observation in df_predictions
df_predictions['mean'] = df_predictions.mean(axis=1)

# place each record into equal sized probability groups using the mean
df_predictions['probability_group'] = pd.qcut(df_predictions['mean'], 10)

# aggregate all predictions for each probability group
d = {}  # dictionary to contain {Interval(probability_group): array([predictions])}

for pg in set(df_predictions.probability_group):
    # combine all predictions for a given group
    frame = df_predictions[df_predictions.probability_group == pg].iloc[:, 0:100]
    d[str(pg)] = frame.as_matrix().flatten()

# create dataframe from all probability group predictions
df_pg = pd.DataFrame(d)
# create boxplots in order of increasing probability ranges
props = dict(boxes='slategray', medians='black', whiskers='slategray')
viz = df_pg.plot.box(color=props, figsize=(15, 7), patch_artist=True, rot=45)
grid = viz.grid(False, axis='x')
ylab = viz.set_ylabel('Readmission Probability')
xlab = viz.set_xlabel('Mean Prediction Probability Ranges')
title = viz.set_title(
    label='Expected Prediction Distributions by Readmission Prediction Range',
    fontsize=18
)