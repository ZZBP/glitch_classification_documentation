from panoptes_client import Panoptes, Project, SubjectSet

def connect_to_panoptes(username, password):
    """
    Connects to the Panoptes platform using specified credentials.
    Hardcoded credentials are used for this connection.

    Args:
        username (str): zooniverse account username
        password (str): password to the account

    Returns:
        None: Establishes connection to the Panoptes API.
    """
    Panoptes.connect(username=username, password=password)
    print("Connection established.")

def create_project(project_display_name, description, private=True):
    """
    Creates a new project on the Panoptes platform with predefined properties.
    Predefined project details are used for the creation of the project.

    Args:
        project_display_name (str): The name of your Zooniverse project
        description (str): A brief summary of the project
        private (boolean): Flag the project to be private/public; default to be true

    Returns:
        new_project: A new project instance that has been saved to the Panoptes platform.
    """
    new_project = Project()
    new_project.display_name = project_display_name
    new_project.description = description
    new_project.primary_language = 'en'
    new_project.private = private
    new_project.save()
    return new_project

def create_subject_set(new_project, subject_set_name):
    """
    Creates a new subject set linked to the specified project.

    Args:
        new_project(Project): A Zooniverse Project instance to which the new subject set will be linked.
        subject_set_name (string): The name of the uploaded subject_set

    Returns:
        subject_set: A new subject set instance that has been saved to the Panoptes platform.
    """

    subject_set = SubjectSet()
    subject_set.links.project = new_project
    subject_set.display_name = subject_set_name
    subject_set.save()
    return subject_set

if __name__ == '__main__':
    # TODO: complete the assignment of the following variables
    username = # Replace with your zooniverse username
    password = # Replace with your zooniverse password
    description = # Replace with your project description

    project_display_name = input("Enter project name: ")
    subject_set_name = input("Enter subject set name: ")

    connect_to_panoptes(username, password)

    new_project = create_project(project_display_name, description)
    print("New project created, with project number :" + str(new_project))
    subject_set = create_subject_set(new_project,subject_set_name )
    print("New subject set created, with project number:" + str(subject_set))

