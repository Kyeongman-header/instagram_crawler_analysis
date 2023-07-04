# imports the Google Cloud client library
import os
from google.cloud import vision
from tqdm import tqdm, trange


# pip install --upgrade google-cloud-vision
# 구글 비전 클라이언트 다운로드

def run_quickstart(path = "pictures") -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient(client_options={"api_key": "",
                                                               "quota_project_id": ""}) # key와 project id를 여기에 각각 넣습니다
    
    file_list = os.listdir(path)
    file_count = len(file_list)
    # file_count=10
    whole_labels=[]
    whole_landmarks=[]
    whole_objects=[]
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
            # response = client.landmark_detection(image=image)
            # landmarks = response.landmark_annotations
            # objects=client.object_localization(image=image).localized_object_annotations

        except Exception as err:
            print(f"cloud api error. {err=}, {type(err)=}")
            continue

        for label in labels:
            whole_labels.append(label.description)
            # print(label.description)
        # for landmark in landmarks:
        #     whole_landmarks.append(landmarks.description)
            # print(landmarks.description)
        # for obj in objects:
        #     # print(obj.name)
        #     whole_objects.append(obj.name)
            
    return whole_labels, whole_objects

import csv


if __name__ == "__main__":
    labels,objects=run_quickstart(path="pictures")
    with open('labels.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        for label in labels:
            mywriter.writerow([label])
    
    # with open('objects_2.csv', 'w', newline='') as file:
    #     mywriter = csv.writer(file, delimiter=',')
    #     for label in labels:
    #         mywriter.writerow([label])
