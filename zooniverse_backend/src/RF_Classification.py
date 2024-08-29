# Authors: Zoey Zhang, Simran Nerval

import pandas as pd
from Data_Export_Downloader import download_exports
import requests
from datetime import datetime
from panoptes_client import Project, Panoptes
import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def extract_feature(subject_data_json, feature_name):
    # Load the JSON
    subject_data = json.loads(subject_data_json)
    # Assuming there is a single key in 'subject_data' that corresponds to the subject, and our features are directly under this key.
    # Adjustments may be required based on the actual JSON structure.
    subject_key = next(iter(subject_data.keys()))
    feature_value = subject_data[subject_key].get(feature_name, None)
    return feature_value

def extract_label(annotations_json):
    annotations = json.loads(annotations_json)
    # Iterate through the list of annotations to find the 'value'
    for annotation in annotations:
        # Assuming each annotation contains a list where the classification is the first item
        if 'value' in annotation:
            label = annotation['value']
            # Map the label to its numerical representation
            return classification_mapping.get(label, -1)  # Returns -1 if the label is not in our mapping
    return -1 

def split_into_training_and_test(df, train_per):

    '''
    Split panadas dataframe into training and test set.

    Input: df: panadas data frame, train_per: percent of the data for training set in decimal form
    Output: df_train: pandas dataframe of the training data, df_test: pandas dataframe of the test data, 
    inds: array of the indicies of the training data in orginal dataframe
    '''

    train_inds = np.random.choice(a = df.shape[0], size = int(df.shape[0]*train_per), replace = False)

    df_train = df.iloc[train_inds]

    df_test = df.drop(df.index[train_inds])

    return df_train, df_test, train_inds

def training_forest(x_train, y_train, n_trees = 50, max_depth = 15):

    '''
    Train random forest.

    Input: df_train: panadas data frame of training data, cols: list of columns of stats to train with
    Optional: n_trees: number of trees in forest (default = 50),
    max_depth: maximum number of splits for each tree (default = 15)
    Output: forest: trained random forest
    '''

    X, Y = x_train, y_train

    forest = RandomForestClassifier(criterion='entropy', n_estimators = n_trees, random_state=1, n_jobs=2, max_depth = max_depth)
    
    forest.fit(X, Y)

    return forest


if __name__ == '__main__':
    username = 'Zoeyyy'
    password = 'mm167261027'
    project_path = 'zoeyyy/test-project-with-python-client'
    dstn_class = '/home/simran/examples_for_zoey/plots_for_labelling/sample_classifications_export.csv'
    output_dir = '/home/simran/examples_for_zoey/plots_for_labelling/menifest.csv'

    project = Project.find(slug=project_path)
    Panoptes.connect(username=username, password=password)
    download_exports(project, dstn_class)

    df = pd.read_csv(dstn_class)

    cols_for_training = ['Number of Detectors', 'Y and X Extent Ratio','Y Hist Max and Adjacent/Number of Detectors',
          'Within 0.1 of Y Hist Max/Number of Detectors', 'Mean abs(Correlation)', 'Mean abs(Time Lag)']

    # Extract each feature from 'subject_data'
    for feature_name in cols_for_training:
        df[feature_name] = df['subject_data'].apply(lambda x: extract_feature(x, feature_name))

    # # Check if the features were correctly extracted
    # df[cols_for_training].head()

    # Define the mapping from classification labels to numerical representations
    classification_mapping = {
        "Point Sources": 0,
        "Point Sources + Other": 1,
        "Cosmic Rays": 2,
        "Other": 3
    }

    df['classification_label'] = df['annotations'].apply(extract_label)

    df.to_csv(output_dir, index=False)

    # # Display the first few rows to verify the changes
    # print(df[['classification_label']].head())

    ############### Training ####################
    df_train, df_test, train_inds = split_into_training_and_test(df, 0.8)

    X_train = df_train[cols_for_training]
    y_train = df_train['classification_label']

    X_test = df_test[cols_for_training]
    y_test = df_test['classification_label']

    forest_train = training_forest(X_train, y_train)

    y_pred = forest_train.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)





