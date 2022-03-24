import os, sys
sys.path.append("..")
from mvpdlite import data_loading, model_exec

"""
Step 1 - Analysis Specification
"""
# Subject/Participant
sub='sub-01'
# Total number of experimental runs
total_run=8

# Functional Data
filepath_func=[]
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run1.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run2.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run3.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run4.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run5.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run6.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run7.nii.gz']
filepath_func+=['./testdata/'+sub+'/'+sub+'_movie_bold_space-MNI152NLin2009cAsym_preproc_denoised_run8.nii.gz']

# Predictor ROI Mask
filepath_mask1='./testdata/'+sub+'/'+sub+'_FFA_80vox_bin.nii.gz'
# Target ROI Mask
filepath_mask2='./testdata/GM_thr0.1_bin.nii.gz'

base1=os.path.basename(filepath_mask1)
base2=os.path.basename(filepath_mask2)
roi_1_name=base1.split('.nii')[0]
roi_2_name=base2.split('.nii')[0]

# Output Directory
roidata_save_dir='./testdata/roi_data/'
results_save_dir='./results/'

# MVPD Model
model_type='L2_LR' # ['PCA_LR', 'L2_LR']

# only for PCA_LR
num_pc=3 # number of principal components used

# only for L2_LR
crossValid=False # cross validation
alpha=0.001 # regularization strength

# Leave k run out
leave_k=1

# Save Settings
save_prediction=False # default

"""
Step 2 - Data Loading
"""
data_loading.load_data(sub, total_run, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, roidata_save_dir)

"""
Step 3 - Analysis Execution
"""
model_exec.MVPD_exec(model_type, sub, total_run, leave_k, alpha, crossValid, num_pc, roidata_save_dir, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, results_save_dir, save_prediction)
