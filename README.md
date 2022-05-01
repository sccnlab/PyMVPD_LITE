# PyMVPD_LITE

This is a lite version of [PyMVPD](https://github.com/sccnlab/PyMVPD) to model the multivariate interactions between brain regions using fMRI data. You can find a description of the MVPD method in this [article](https://doi.org/10.1371/journal.pcbi.1005799).

[NEW!] We added a preprint with detailed descriptions about the toolbox and example applications. Check it out [here](https://biorxiv.org/cgi/content/short/2021.10.12.464157v1)!

## MVPD Model Family
1. Linear Regression (LR) Models

Available built-in model components:
* Dimensionality reduction: principal component analysis ([PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)), independent component analysis ([ICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html))
* Regularization: [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) (L1), [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) (L2), [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html) (L2 with built-in cross-validation)
* Cross validation: leave k run out

  Example LR models:
  * [L2_LR](https://github.com/sccnlab/PyMVPD_LITE/tree/main/exp/run_MVPD_L2_LR.py): linear regression model with L2 regularization
  * [PCA_LR](https://github.com/sccnlab/PyMVPD_LITE/tree/main/exp/run_MVPD_PCA_LR.py): linear regression model with PCA but no regularization

In addition to the above built-in functions, you can also customize your own functions by adding scripts under [mvpdlite/custom_func](https://github.com/sccnlab/PyMVPD_LITE/tree/main/mvpdlite/custom_func).

## Workflow
<img src="/PyMVPD_LITE_workflow.png" width="750"/>

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

## Tutorial
### Test Dataset
[Data](https://github.com/sccnlab/PyMVPD_LITE/tree/main/exp/testdata) of one subject from the [_StudyForrest_](http://studyforrest.org) dataset.

Predictor ROI: FFA - fusiform face area, 

Target ROI: GM - gray matter.

* Raw data were first preprocessed using [fMRIPrep](https://fmriprep.readthedocs.io/en/latest/index.html) and then denoised by using CompCor (see more details in [Fang et al. 2019](https://doi.org/10.31234/osf.io/qbx4m)).

### Example Analyses and Scripts
To give a quick try for MVPD analysis, you can directly run our example script [run_MVPD_test.py](https://github.com/sccnlab/PyMVPD_LITE/blob/main/exp/run_MVPD_test.py) or other example MVPD models under [exp/](https://github.com/sccnlab/PyMVPD_LITE/blob/main/exp/) (e.g. run_MVPD_xxx.py):
```
cd exp/
python3 run_MVPD_test.py
```

We have also provided a [tutorial](https://github.com/sccnlab/PyMVPD_LITE/blob/main/exp/PyMVPD_LITE_Tutorial.ipynb) in jupyter notebook. Feel free to check it out!

## Customization
To customize and run your own MVPD model, please follow the three steps:
```
import os
from mvpdlite import data_loading, model_exec
```
Step 1 - Analysis Specification
```
# Model Input Info
inputinfo=data_loading.structtype()
inputinfo.sub='sub-01' # subject whose data are to be analyzed
filepath_func=[] # input functional Data
filepath_func+=['path/to/functional/data/run1.nii.gz']
filepath_func+=['path/to/functional/data/run2.nii.gz']
......

inputinfo.filepath_mask1='path/to/predictor/ROI/mask.nii.gz' # predictor ROI mask
inputinfo.filepath_mask2='path/to/target/ROI/mask.nii.gz' # target ROI mask

inputinfo.roidata_save_dir='path/to/save/roidata/' # output data directory
inputinfo.results_save_dir='path/to/save/results/' # output model results directory
inputinfo.save_prediction=False # whether to save predicted timecourses in the target ROI

# MVPD Model Parameters
params=data_loading.structtype()
params.leave_k=1 # cross validation: leave k run out, default=1

### LR model parameters
......

```
Step 2 - Data Loading
```
data_loading.load_data(inputinfo)
```
Step 3 - Analysis Execution
```
model_exec.MVPD_exec(inputinfo, params)
```
### Required Input Information 
- **inputinfo.sub**
  - This variable specifies the subject whose data are to be analyzed.
- **input.filepath_func**
  - This variable specifies the list of paths to the directories containing processed functional data.
- **inputinfo.filepath_mask1**
  - This variable specifies the path to the directory containing the predictor ROI mask.
- **inputinfo.filepath_mask2**
  - This variable specifies the path to the directory containing the target ROI mask.
- **inputinfo.roidata_save_dir**
  - This variable specifies the path to the directory where the extracted functional data will be saved.
- **inputinfo.results_save_dir**
  - This variable specifies the path to the directory where the results will be saved.
- **inputinfo.save_prediction** 
  - This variable specifies whether to save predicted timecourses in the target ROI.

### List of Model Parameters

NOTICE: Remember to set the value of the parameter manually if you do not want to use the default value.

- General model parameters
  - **params.leave_k**
    - This parameter determines the number of leave out runs in cross-validation.
    - The default value is 1 (leave-one-run-out procedure).

- LR model parameters
  - **params.dim_reduction**: 
    - This parameter determines whether dimensionality reduction is applied to the input data.
    - It is only used if you are using a linear regression model by setting params.mode_class='LR'
    - The default value is false.
  - **params.dim_type**: 
    - This parameter determines the type of the dimensionality reduction.
    - It is only used if you are using a linear regression model and you set "params.dim_reduction=True".
    - The available values are 'pca', 'ica', or the name of your custom dimensionality reduction method.
    - The default value is 'pca'.
  - **params.num_dim**:
    - This parameter determines the number of dimensions to keep after dimensionality reduction.
    - It is only used if you are using a linear regression model and you set "params.dim_reduction=True".
    - The default value is 3.
    
  - **params.lin_reg**:
    - This parameter determines whether to add a regularization term to the linear regression model.
    - It is only used if you are using a linear regression model by setting params.mode_class='LR'.
    - The default value is false.
  - **params.reg_type**
    - This parameter determines the type of regularization term that you want to add to the linear regression model.
    - It is only used if you are using a linear regression model with regularization by setting "params.mode_class='LR', params.lin_reg=True".
    - The available values are 'Ridge', 'Lasso', and 'RidgeCV'.
    - The default value is 'Ridge'.
  - **params.reg_strength**
    - This parameter determines the regularization strength of the chosen regularization term.
    - It is only used if you are using a linear regression model with regularization by setting "params.mode_class='LR', params.lin_reg=True".
    - The default value is '0.001'.
  - **params.reg_strength_list**
    - This parameter determines the array of regularization strength values to try in the cross-validation for Ridge regression.
    - It is only used if you are using a linear RidgeCV regression model by setting "params.mode_class='LR', params.lin_reg=True, params.reg_type='RidgeCV'".
    - The default array is [0.001, 0.01, 0.1].

## Citation
PyMVPD has been used in:

- PyMVPD: A toolbox for multivariate pattern dependence. [PDF](https://www.biorxiv.org/content/10.1101/2021.10.12.464157v1.full.pdf) <br/>
Fang, M., Poskanzer, C., Anzellotti, S.

- Identifying hubs that integrate responses across multiple category-selective regions.<br/>
Fang, M., Aglinskas, A., Li, Y., Anzellotti, S. 

If you plan to use the toolbox, please consider citing this.

```
@article{fang2021pymvpd,
  title={PyMVPD: A toolbox for multivariate pattern dependence},
  author={Fang, Mengting and Poskanzer, Craig and Anzellotti, Stefano},
  journal={bioRxiv},
  year={2021},
  publisher={Cold Spring Harbor Laboratory}
}
```

## Contact
Reach out to Mengting Fang (mtfang0707@gmail.com) for questions, suggestions and feedback!
