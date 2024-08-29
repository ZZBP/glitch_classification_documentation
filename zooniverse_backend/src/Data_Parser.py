import pandas as pd
import json

def extract_glitch_value(annotation_json):
    annotations = json.loads(annotation_json)
   
    if annotations and 'value' in annotations[0]:
        return annotations[0]['value']
    return None

def modify_subject_data(subject_data_json, glitch_value, annotator_name):
    subject_data = json.loads(subject_data_json)
    
    for key in subject_data.keys():
        print(key)
    #     if "Glitch" in subject_data[key]:
    #         subject_data[key]["Glitch"] = glitch_value
    #     subject_data[key]["annotator"] = annotator_name

    # return json.dumps(subject_data)

def flatten_subject_data(subject_data_json):
    subject_data_dict = json.loads(subject_data_json)
    key = next(iter(subject_data_dict))
    return subject_data_dict[key]

if __name__ == '__main__':
    # TODO: complete the assignment of the following variable
    file_path = # Replace with the file path to exported classification file
    
    df = pd.read_csv(file_path)
    df['glitch'] = df['annotations'].apply(extract_glitch_value)
    df['annotator'] = df['user_name']
    df['subject_data'] = df.apply(lambda row: modify_subject_data(row['subject_data'], row['glitch'], row['annotator']), axis=1)

