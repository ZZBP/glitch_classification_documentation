import requests
from datetime import datetime
from panoptes_client import Project, Panoptes

def download_file(url, dstn):
    """
    Downloads a file from the specified URL to a destination path.

    Args:
        url: URL of the file to be downloaded.
        dstn: Destination path where the file will be saved.

    Returns:
        str: Path to the downloaded file.
    """
    request = requests.get(url, stream=True)
    with open(dstn, 'wb') as dstn_f:
        for chunk in request.iter_content(chunk_size=4096):
            dstn_f.write(chunk)
    return dstn


def download_exports(projt, dstn_cl):
    """
    Downloads the latest classification and subject exports for a given project.

    Args:
        projt: Project instance from which the exports will be downloaded.
        dstn_cl: Destination path for the classification export file.

    Returns:
        bool: Indicates whether the files were successfully downloaded.
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

if __name__ == '__main__':
    # TODO: complete the assignment of the following variables
    username = # Replace with your zooniverse username
    password = # Replace with your zooniverse password
    project_path = # Replace with your zooniverse project path which is in the format of username/projectname
    dstn_class = # Replace with the file path where you want to store the export
    
    Panoptes.connect(username=username, password=password)
    project = Project.find(slug=project_path)

    print(download_exports(project, dstn_class))