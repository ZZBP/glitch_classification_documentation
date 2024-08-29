from panoptes_client import Panoptes, Project, SubjectSet
import re

def format_string(input_string):
    """
    Parse strings into zooniverse project link format.
    
    Args:
        input_string(str): the Zooniverse project name
    """
    # Convert to lowercase
    formatted_string = input_string.lower()
    # Replace spaces with hyphens
    formatted_string = formatted_string.replace(" ", "-")
    # Remove invalid characters (keep only letters, numbers, and hyphens)
    formatted_string = re.sub(r"[^a-z0-9-]", "", formatted_string)
    # Replace multiple hyphens with a single hyphen
    formatted_string = re.sub(r"-+", "-", formatted_string)
    return formatted_string

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
    project = Project.find(23577)

    print(f"Project with project id: {project}")
    subject_set.links.project = project
    subject_set.display_name = subject_set_name
    subject_set.save()
    return subject_set

if __name__ == '__main__':
    # TODO: complete the assignment of the following variables
    username = # Replace with your zooniverse username
    password = # Replace with your zooniverse password
    subject_set_name = input("Enter subject set name: ")

    Panoptes.connect(username=username, password=password)
    print("Connection established.")

    subject_set = create_subject_set(subject_set_name)
    print("New subject set created, with subject_set number:" + str(subject_set))