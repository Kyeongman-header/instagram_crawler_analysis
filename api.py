


# imports the Google Cloud client library
import os
from google.cloud import vision
from tqdm import tqdm, trange


def run_quickstart(path = "pictures") -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient(client_options={"api_key": "",
                                                               "quota_project_id": ""})
    
    file_list = os.listdir(path)
    file_count = len(file_list)
    whole_labels=[]
    # The name of the image file to annotate
    for i in trange(file_count):
        try:
            file_name = os.path.abspath(path+"/test__"+str(i)+".jpg")

        #     # Loads the image into memory
            with open(file_name, "rb") as image_file:
                content = image_file.read()
        except:
            print("file open error.")
            continue
        try:
            image = vision.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations
        except Exception as err:
            print(f"cloud api error. {err=}, {type(err)=}")
            continue

        for label in labels:
            whole_labels.append(label.description)
            # print(label.description)

    return whole_labels

import csv


if __name__ == "__main__":
    labels=run_quickstart(path="pictures")
    with open('labels.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        for label in labels:
            mywriter.writerow([label])
    
