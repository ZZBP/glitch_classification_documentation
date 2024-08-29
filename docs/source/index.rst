Welcome to Glitch Classification with Zooniverse tutorial!
===================================

This is a step by step tutorial to demonstrate how you may set up a project on Zooniverse to facilitate your research that involves classification.

src
---

.. toctree::
   :maxdepth: 2

   data_exporters
   data_operations

data_exporters
--------------

This directory contains scripts related to the exporting of data.

Data_Export_Downloader.py
   This script handles the downloading of data exports from a specified source.

Data_Export_Generator.py
   This script is responsible for generating data exports based on user queries or automated system triggers.

Data_Parser.py
   Parses data files and prepares them for further processing or storage.

Data_Upload.py
   Manages the uploading of data to specified servers or databases.

Duplicate_Removal.py
   Identifies and removes duplicate entries within data sets to ensure the integrity of the data.

data_operations
---------------

manifest.csv
   A CSV file listing all data items processed or handled by the system, serving as a manifest.

Metadata_Update.py
   Updates the metadata associated with data items, ensuring that metadata reflects the latest changes.

Project_Initializer.py
   Initializes new projects within the backend system, setting up necessary configurations and directories.

RF_Classification.py
   Implements a Random Forest classification algorithm on specified data sets.

Subject_Set_Creator.py
   Automates the creation of subject sets for data processing and analysis tasks.

Other Files
-----------

LICENSE
   Contains the licensing information for the project.

README.md
   Provides an overview of the project, setup instructions, and other necessary information for users and developers.
