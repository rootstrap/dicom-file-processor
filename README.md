# DICOM file processor

Reads a DICOM file, generates a folder with patient info and exports images from file on it.
This project uses [pydicom](https://pydicom.github.io/pydicom/stable/index.html).

## Pydicom installation

It's recommended to use [Anaconda](https://docs.anaconda.com/anaconda/install/mac-os/) to avoid problems when installing [gdcm](http://gdcm.sourceforge.net/wiki/index.php/Main_Page).  
After a successful installation of anaconda, generate a conda environment in the project folder and activate it:

```python
>> conda create --name dicom-file-processor python=3.7

>> conda activate dicom-file-processor
```

Now install pydicom and some of the most used libraries:

```python
# Pydicom
>>> conda install -c conda-forge pydicom

# Numpy
>>> conda install numpy

# Pillow
>>> conda install -c conda-forge openjpeg jpeg
>>> conda install pillow

# CharPyLS
>>> conda install cython
>>> pip install git+https://github.com/Who8MyLunch/CharPyLS

# GDCM
>>> conda install gdcm -c conda-forge
```

## Extracted data

The `file-processor` script stores a dict in `patients-data` folder that contains patient info and the image/images in the pixel_array of the DICOM file.
