import subprocess
from panoptes_client import Panoptes, Project, SubjectSet
import re

def create_subject_set(subject_set_name):
    """
    Creates a new subject set linked to the specified project.

    Args:
        project_id(int): ID of the interested Zooniverse project to which the new subject set will be linked.
        subject_set_name (string): The name of the uploaded subject_set

    Returns:
        subject_set: A new subject set instance that has been saved to the Panoptes platform.
    """

    subject_set = SubjectSet()
    # project = Project.find(slug='projects/zoeyyy/{}'.format(project_name))
    project = Project.find(23577) # project id 

    print(f"Project with project id: {project}")
    subject_set.links.project = project
    subject_set.display_name = subject_set_name
    subject_set.save()
    return subject_set

def extract_subject_set_id(subject_set_str):
    match = re.search(r'\d+', subject_set_str)
    if match:
        return match.group()
    else:
        raise ValueError("No numeric ID found in subject set string")

def run_bash_command(command, shell='/bin/bash'):
    print(f"Running command: {command}")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable=shell, text=True)

    # Read the output in real-time
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    
    # Capture any remaining error output
    stderr = process.stderr.read()
    if stderr:
        print(f"Command error: {stderr.strip()}")
    
    return process.returncode

def upload_subjects(subject_set_id, file_path):
    command = f"panoptes subject-set upload-subjects {subject_set_id} {file_path}"
    return run_bash_command(command)

def main():
    # TODO: complete the assignment of the following variables
    username = # Replace with your zooniverse username
    password = # Replace with your zooniverse password

    subject_set_name = input("Enter subject set name: ")

    Panoptes.connect(username=username, password=password)
    print("Connection established.")

    subject_set = create_subject_set(subject_set_name)
    subject_set_id = subject_set.id 
    print("New subject set created, with subject_set number:" + subject_set_id)

    # Get user inputs
    file_path = input("Enter the file path to the manifeset.csv: ")

    # Run the command
    return_code = upload_subjects(subject_set_id, file_path)
    
    # Check return code
    if return_code == 0:
        print("Command executed successfully.")
    else:
        print("Command failed with return code:", return_code)

if __name__ == "__main__":
    main()
