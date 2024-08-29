import time
from datetime import datetime
from panoptes_client import Project, Panoptes

def generate_class(projt):
    """
    Requests and checks the generation of a classifications export for a given project.

    Args:
        projt: Project instance for which the classifications export will be generated.

    Returns:
        bool: Indicates whether the export was successfully generated.
    """
    try:
        print('tried')
        meta_class = projt.describe_export('classifications')
        if not meta_class:
            print('exportation requested')
        last_generated = meta_class['media'][0]['updated_at'][0:19]
        tdelta = (datetime.now() - datetime.strptime(last_generated, '%Y-%m-%dT%H:%M:%S')).total_seconds()
        # if (240 + tdelta / 60) >= 24 * 60:  # 300 is offset EST offset from Zulu  could be 240 during EDT
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
        # else:
        #     print(str(datetime.now())[0:19] + ' Too soon to generate Classification export - ' +
        #           str(round((tdelta / 3600 + 5), 1)) + '  hrs.')
        #     return False
    except Exception as e:
        print(f"Error occurred: {e}")

        print(str(datetime.now())[0:19] + ' Classification export did not generate correctly')
        return False


def generate_subj(projt):
    """
    Requests and checks the generation of a subjects export for a given project.

    Args:
        projt: Project instance for which the subjects export will be generated.

    Returns:
        bool: Indicates whether the export was successfully generated.
    """
    try:
        meta_subj = projt.describe_export('subjects')
        last_generated = meta_subj['media'][0]['updated_at'][0:19]
        tdelta = (datetime.now() - datetime.strptime(last_generated, '%Y-%m-%dT%H:%M:%S')).total_seconds()
        # if (240 + tdelta / 60) >= 24 * 60:  # 300 is offset EST offset from Zulu  could be 240 during EDT
        project.generate_export('subjects')
        print('Export request sent, please wait 30 seconds to verify generation has begun')
        time.sleep(30)
        meta_subj = projt.describe_export('classifications')
        now_generated = meta_subj['media'][0]['updated_at'][0:19]
        tdelta_now = (datetime.now() - datetime.strptime(now_generated, '%Y-%m-%dT%H:%M:%S')).total_seconds()
        if tdelta_now < 100:
            print(str(datetime.now())[0:19] + ' Subject export generated.')
            return True
        else:
            print(str(datetime.now())[0:19] + ' Subject export did not generate correctly')
            return False
        # else:
        #     print(str(datetime.now())[0:19] + ' Too soon to generate Subject export - ' +
        #           str(round((tdelta / 3600 + 5), 1)) + '  hrs.')
        #     return False
    except:
        print(str(datetime.now())[0:19] + ' Subject export did not generate correctly')
        return False

if __name__ == '__main__':
    # TODO: complete the assignment of the following variables
    username = # Replace with your zooniverse username
    password = # Replace with your zooniverse password
    project_path = # Replace with your zooniverse project path which is in the format of username/projectname

    Panoptes.connect(username=username, password=password)
    project = Project.find(slug=project_path)
    print(generate_class(project))
