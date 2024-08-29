Data Exports through Panoptes Client
====================================

After labeling, exporting the data is crucial for further analysis and processing. This section outlines how to handle data exports using the Panoptes client.

Exporting Classification Data
-----------------------------

Here's how to request and check the status of a classifications export:

.. code-block:: python

   def generate_class(projt):
       """
       Requests a classifications export for a project and checks its generation status.

       Args:
           projt: Project instance for which the export is requested.

       Returns:
           bool: True if the export was successfully generated, False otherwise.
       """
       # Implementation details

Downloading Exports
-------------------

After the classification data is ready, it can be downloaded using the following function:

.. code-block:: python

   def download_exports(projt, dstn_cl):
       """
       Downloads the latest classification and subject exports for a project.

       Args:
           projt: Project instance from which the exports will be downloaded.
           dstn_cl: Destination path for the classification export file.

       Returns:
           bool: True if files were successfully downloaded, False otherwise.
       """
       # Implementation details
