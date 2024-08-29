# Zooniverse_Glitch_Classification
This document provides an overview of the main functionalities and functions included in each Python file created for managing projects, subject sets, and data exports in Panoptes.

## Installation 

Make sure you have installed python3 by checking
`$ python --version && pip --version`

Then run the following to install zooniverse Python client
`$ pip install panoptescli`

## Project Structure 
## 1. Project Initializer

### Main Functionality:

Create a new instance of a Zooniverse project and upload an initial subject set to the project.

## 2. Data Export Generator

### Main Functionality:

Contains functions for requesting and generating exports for classifications and subjects.

## 3. Data Export Downloader

### Main Functionality:

Facilitates downloading of classification and subject export files from a specified Panoptes project.

## 4. Duplicate Removal

### Main Functionality:

Removes duplicate subjects from a subject set based on a specified metadata field.

## 5. Subject Set Metadata Update

### Main Functionality:

Updates the metadata for subjects in a subject set based on information from a CSV file.
