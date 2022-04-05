# fingercode-matching
Fingerprint matching based on the fingercodes.

## Fingercode extraction

The dataset used for the fingerprints it's available here: https://neurotechnology.com/download/CrossMatch_Sample_DB.zip and it contains a total of 408 .tif images. Originally the dataset contains 8 different images for each fingerprint and about 6 different fingers for each person. I will treat the different fingers as fingers belonging to distinct persons, so the dataset will contain fingerprints from 51 individuals.

In the folder "fingercode_extraction" you will find the MATLAB algorithm developed by Luigi Rosa (https://github.com/hbhdytf/fingercode) that allows to extract the fingercode starting from a fingerprint image. It uses a bank of Gabor filters to capture both local and global details in a fingerprint as a compact fixed length fingercode. This algorithm takes around 0.35 seconds for each image to be processed in order to extract the fingercode. Firstly it finds out the core point of the fingerprint image and around that it builds 5 concentric bands (wide 20 pixels each) all composed by 16 arcs but avoiding the inner circle of radius equal to 12 pixels (the central band is not considered because it is a too small area). Afterwars it uses 8 Gabor filters so the final fingercode will contain 1280 "bits" obtained by concatenating the results of two different rotations of the image (2(n_bands*n_arcs*n_Gabor_filters)).

You will find the .zip folder already containing all the fingercodes extracted from the images.

## Fingercode recognition

In this folder you will find a brief Jupiter notebook; it will use the content of *train* and *test* folders to perform an identification scenario.
The matching is done using the Euclidean distance among the fingercodes.
