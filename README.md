# PyMVPD_LITE

This is a lite version of [PyMVPD](https://github.com/sccnlab/PyMVPD) to model the multivariate interactions between brain regions using fMRI data. You can find a description of the MVPD method in this [article](https://doi.org/10.1371/journal.pcbi.1005799).

[NEW!] We added a preprint with detailed descriptions about the toolbox and example applications. Check it out [here](https://biorxiv.org/cgi/content/short/2021.10.12.464157v1)!

## MVPD Model Family
1. Linear Regression (LR) Models
Available built-in model components:
* Dimensionality reduction: principal component analysis ([PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)), independent component analysis ([ICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html))
* Regularization: [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) (L1), [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) (L2), [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html) (L2 with build-in cross-validation)
* Cross validation: leave k run out

Example LR models:
* L2_LR: linear regression model with L2 regularization
* PCA_LR: linear regression model with PCA but no regularization

In addition to these build-in functions, you can also customize your own MVPD models by adding scripts under [mvpdlite/](https://github.com/sccnlab/PyMVPD_LITE/tree/main/mvpdlite).

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
To give a quick try for MVPD analysis, you can directly run our example script [run_MVPD.py](https://github.com/sccnlab/PyMVPD_LITE/blob/main/exp/run_MVPD.py):
```
cd exp/
python3 run_MVPD.py
```

We have also provided a [tutorial](https://github.com/sccnlab/PyMVPD_LITE/blob/main/exp/PyMVPD_LITE_Tutorial.ipynb) in jupyter notebook. Feel free to check it out!

## Customization
To generate your own scripts, please follow the three steps:
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
params.dim_reduction=True # whether to perform dimensionality reduction on input data
params.dim_type='pca' # ['pca'(default), 'ica']
params.num_dim=3 # number of dimensions after dimensionality reduction, default=3

params.lin_reg=True # whether to add regularization term
params.reg_type='Ridge' # ['Ridge'(default), 'Lasso', 'RidgeCV']
params.reg_strength=0.001 # regularization strength, default=0.001
#params.reg_strength_list=[0.1,1.0,10.0] # only for RidgeCV: array of reg_strength values to try, default=(0.1,1.0,10.0)

```
Step 2 - Data Loading
```
data_loading.load_data(inputinfo)
```
Step 3 - Analysis Execution
```
model_exec.MVPD_exec(inputinfo, params)
```

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
