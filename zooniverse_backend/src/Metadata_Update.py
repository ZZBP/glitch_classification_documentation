import csv
from panoptes_client import SubjectSet, Panoptes, Workflow, Caesar
import pandas as pd
import json


def update_metadata(set_id, metadata_csv):
    """
    Updates the metadata for all subjects in the specified subject set based on information from a CSV file.

    Args:
        set_id: ID of the subject set whose subjects' metadata will be updated.
        metadata_csv: Path to the CSV file containing the new metadata information.

    Returns:
        int: Count of subjects whose metadata was updated.
    """
    subject_set = SubjectSet.find(set_id)
    with open(metadata_csv, mode='r') as infile:
        reader = csv.DictReader(infile)
        metadata_dict = {row['#File']: row for row in reader}

    updated_count = 0
    for subject in subject_set.subjects:
        file_name = subject.metadata.get('#file')
        if file_name and file_name in metadata_dict:
            new_metadata = metadata_dict[file_name]
            subject.metadata.clear()
            subject.metadata.update(new_metadata)
            subject.save()
            updated_count += 1
            print(f"Updated {updated_count} subjects.")
    return updated_count


# def retirement():
#     """
#     Backup function to manually retire subjects.
#     """
#     workflow.retire_subjects(1234) 
#     workflow.retire_subjects([1,2,3,4]) 
#     workflow.retire_subjects(Subject(1234)) 
#     workflow.retire_subjects([Subject(12), Subject(34)])

if __name__ == '__main__':
    # TODO: complete the assignment of the following variables
    username = # Replace with your zooniverse username
    password = # Replace with your zooniverse password
    workflow_id = # Replace with your workflow id
    subject_set_id = # Replace with the subject set that you wish to find
    file_path = # Replace with the file path to exported classification file

    Panoptes.connect(username=username, password=password)
    print("Connection established.")

    caesar = Caesar()
    caesar.save_workflow(workflow_id)
    workflow = Workflow(workflow_id)
    
    subject_set=SubjectSet.find(subject_set_id) 
    df = pd.read_csv(file_path, converters={'subject_data': json.loads})

    targets = list(df['subject_ids'])
    workflow.retire_subjects(targets)
    for target in targets:
        print(f"{target} retired")

