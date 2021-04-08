# PyMVPD LITE

PyMVPD LITE: A LITE version of MultiVariate Pattern Dependence (MVPD) analysis in Python

## MVPD Model Family
1. Linear Regression Models
* L2_LR: linear regression model with L2 regularization
* PCA_LR: linear regression model with no regularization after principal component analysis (PCA)

## Installation & Dependencies
The easiest way to install the package is to execute (possibly in a [new virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments)) the following command:
```
pip install PyMVPD-LITE
```
You can also install from the GitHub [repository](https://github.com/sccnlab/PyMVPD_LITE) to get the most up-to-date version.
```
git clone https://github.com/sccnlab/PyMVPD_LITE.git
pip install -r requirements.txt
```
The following packages need to be installed to use PyMVPD LITE:
* python >= 3.6
* nibabel>=3.2.1
* numpy>=1.19.3
* scikit-learn>=0.20.1
* scipy>=1.1.0

## Usage example
### Test Dataset
[Data](https://github.com/sccnlab/PyMVPD_LITE/tree/main/exp/testdata) of one subject from the [_StudyForrest_](http://studyforrest.org) dataset.

Predictor ROI: FFA - fusiform face area, 

Target ROI: GM - gray matter.

* Raw data were first preprocessed using [fMRIPrep](https://fmriprep.readthedocs.io/en/latest/index.html) and then denoised by using CompCor (see more details in [Fang et al. 2019](https://doi.org/10.31234/osf.io/qbx4m)).

### Example Analyses and Scripts
To give a quick try for MVPD analysis, you can directly run our example script [run_MVPD.py](https://github.com/sccnlab/PyMVPD_LITE/blob/main/exp/run_MVPD.py):
```
cd exp/
python3 run_MVPD.py
```
You can also generate your own scripts following the three steps:
```
import os
from mvpdlite import data_loading, model_exec
```
Step 1 - Analysis Specification
Specify the subject whose data are to be analyzed, the total number of experimental runs, the functional data and ROI masks, the output directory, the type of MVPD model to be used and the model hyperparameters.
```
sub='sub-01' # subject to analyze
total_run=XX # total number of experimental runs

# Input functional Data
filepath_func=[]
filepath_func+=['path/to/functional/data/run1.nii.gz']
filepath_func+=['path/to/functional/data/run2.nii.gz']
......

# Input predictor ROI mask and target ROI mask
filepath_mask1='path/to/predictor/ROI/mask.nii.gz'
filepath_mask2='path/to/target/ROI/mask.nii.gz'

base1=os.path.basename(filepath_mask1)
base2=os.path.basename(filepath_mask2)
roi_1_name=base1.split('.nii')[0]
roi_2_name=base2.split('.nii')[0]

# Output Directory
roidata_save_dir='path/to/save/roidata/'
results_save_dir='path/to/save/results/'

# Choose MVPD model
model_type='L2_LR' # ['PCA_LR', 'L2_LR']

# Set model parameters
# Only for PCA_LR
num_pc=3 # number of principal components used 
# Only for L2_LR
alpha=0.01 

# Save predicted timecourses
save_prediction=False # default
```
Step 2 - Data Loading
```
data_loading.load_data(sub, total_run, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, roidata_save_dir)
```
Step 3 - Analysis Execution
```
model_exec.MVPD_exec(model_type, sub, total_run, alpha, num_pc, roidata_save_dir, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, results_save_dir, save_prediction)
```

## Contact
Reach out to Mengting Fang (mtfang0707@gmail.com) for questions, suggestions and feedback!
