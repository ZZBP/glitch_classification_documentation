from panoptes_client import SubjectSet, Panoptes
import os

def remove_duplicates(subject_set_id, metadata_field):
    """
    Removes duplicate subjects from the specified subject set based on a specified metadata field.

    Args:
        subject_set_id: ID of the subject set from which duplicates will be removed.
        metadata_field: Metadata field used to identify duplicates.

    Returns:
        dict: Contains counts of unique subjects, no metadata count, duplicate count, removed count, and not removed subjects.
    """
    try:
        subject_set = SubjectSet.find(subject_set_id)
        dup_count = 0
        no_metadata = 0
        duplicate_subjects = []
        not_removed = []
        subject_list = set()
        for subject in subject_set.subjects:
            try:
                if subject.metadata[metadata_field] in subject_list:
                    dup_count += 1
                    duplicate_subjects.append(subject.id)
                    try:
                        subject_set.remove(subject.id)
                    except Panoptes.PanoptesAPIException:
                        not_removed.append(subject.id)
                else:
                    subject_list.add(subject.metadata[metadata_field])
            except KeyError:
                no_metadata += 1
        return {
            'unique_subjects_count': len(subject_list),
            'no_metadata_count': no_metadata,
            'duplicate_count': dup_count,
            'removed_count': len(duplicate_subjects) - len(not_removed),
            'not_removed': not_removed
        }
    except Panoptes.PanoptesAPIException as e:
        print(f"Error occurred: {e}")
        return None

# Function that can be used to double check the remaining subjects after the removals

def list_remaining_subjects(subject_set_id, output_directory):
    """
    Creates a CSV file listing all remaining subjects in the specified subject set.

    Args:
        subject_set_id: ID of the subject set from which to list subjects.
        output_directory: Directory where the output CSV will be saved.

    Returns:
        str: Path to the generated CSV file.
    """
    subject_set = SubjectSet.find(subject_set_id)
    output_file_path = os.path.join(output_directory, f"{subject_set.display_name}_subjects.csv")
    with open(output_file_path, 'w') as file:
        for subject in subject_set.subjects:
            metadata_values = list(subject.metadata.values())
            if metadata_values:  # Check if there is metadata to avoid errors
                file.write(f"{subject.id},{metadata_values[0]}\n")
    return output_file_path

if __name__ == '__main__':
    subject_set_id = input('Enter subject set id to remove duplicates: ')
    metadata_field = input('Enter the metadata field to use for checking duplicates: ')
    results = remove_duplicates(subject_set_id, metadata_field)
    if results:
        print('Removal results:', results)

