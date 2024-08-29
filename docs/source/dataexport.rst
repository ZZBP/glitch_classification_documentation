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
        try:
        print('tried')
        meta_class = projt.describe_export('classifications')
        if not meta_class:
            print('exportation requested')
        last_generated = meta_class['media'][0]['updated_at'][0:19]
        tdelta = (datetime.now() - datetime.strptime(last_generated, '%Y-%m-%dT%H:%M:%S')).total_seconds()
        print('reached if statement')
        project.generate_export('classifications')
        print('Export request sent, please wait 30 seconds to verify generation has begun')
        time.sleep(30)
        meta_class = projt.describe_export('classifications')
        now_generated = meta_class['media'][0]['updated_at'][0:19]
        tdelta_now = (datetime.now() - datetime.strptime(now_generated, '%Y-%m-%dT%H:%M:%S')).total_seconds()
        if tdelta_now < 100:
            print(str(datetime.now())[0:19] + ' Classification export generated.')
            return True
        else:
            print(str(datetime.now())[0:19] + ' Classification export did not generate correctly')
            return False
        
        except Exception as e:
            print(f"Error occurred: {e}")

            print(str(datetime.now())[0:19] + ' Classification export did not generate correctly')
            return False

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
       # replace path and filename strings for where you want the exports saved in the next two lines:
       try:
        meta_class = projt.describe_export('classifications')
        print(meta_class)
        generated = meta_class['media'][0]['updated_at'][0:19]
        tdelta = (datetime.now() - datetime.strptime(generated, '%Y-%m-%dT%H:%M:%S')).total_seconds()
        age = (300 + int(tdelta / 60))
        print(str(datetime.now())[0:19] + '  Classifications export', age, ' hours old')
        url_class = meta_class['media'][0]['src']
        print(url_class)
        file_class = download_file(url_class, dstn_cl)
        print(str(datetime.now())[0:19] + '  ' + file_class + ' downloaded')
        except:
            print(str(datetime.now())[0:19] + '  Classifications download did not complete')
            return False

   
        return True

Usage Example
-------------

To establish a connection to the Zooniverse backend and generate a subject set:

.. code-block:: python

    Panoptes.connect(username='your_username', password='your_password')
    project = Project.find(slug=project_path)

    print(download_exports(project, dstn_class))