import json

from pydicom import dcmread
from os import mkdir
from os.path import exists
import matplotlib.pyplot as plt
from PIL import Image


# Define path to load the file
FILE_NAME = 'bmode.dcm'
FILE_PATH = f'dicom-files/{FILE_NAME}'


def create_patient_folder(dataset):
    patient_fields = [field for field in dataset.dir() if 'Patient' in field]
    patient_id = None
    folder_name = None
    if 'PatientID' in patient_fields:
        patient_id = dataset['PatientID'].value
        patient_dict = {}
        for field in patient_fields:
            patient_dict[field] = str(dataset[field])
        folder_name = f'patients-data/{patient_id}'
        if not exists(folder_name): 
            mkdir(folder_name)
        with open(f'{folder_name}/patient-info.txt', 'w') as txt_file:
            txt_file.write(json.dumps(patient_dict, indent=4))
            txt_file.close()
    return patient_id, folder_name


def export_images(patient_id, folder_name, dataset):
    if 'PixelData' in dataset:
        # One image case
        if len(dataset.pixel_array.shape) == 3:
            im = Image.fromarray(dataset.pixel_array[0])
            im.save(f'{folder_name}/{patient_id}.jpg')
        # Set of images case
        elif len(dataset.pixel_array.shape) == 4:
            for img_number, img_arr in zip(range(len(dataset.pixel_array)), dataset.pixel_array):
                im = Image.fromarray(img_arr)
                im.save(f'{folder_name}/{patient_id}_{img_number}.jpg')


dataset = dcmread(FILE_PATH)

patient_id, folder_name = create_patient_folder(dataset)

export_images(patient_id, folder_name, dataset)

