import numpy as np
from mvpd.MVPD_L2_LR import run_L2_LR
from mvpd.MVPD_PCA_LR import run_PCA_LR
from mvpd.avgrun_regression import avg_runs

def MVPD_exec(model_type, sub, total_run, alpha, num_pc, roidata_save_dir, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, results_save_dir, save_prediction):
    if model_type == "L2_LR":
       print("\nstart running L2_LR model for", sub)
       run_L2_LR(model_type, sub, total_run, alpha, roidata_save_dir, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, results_save_dir, save_prediction)
    elif model_type == "PCA_LR":
       print("\nstart running PCA_LR model for", sub)
       run_PCA_LR(model_type, sub, total_run, num_pc, roidata_save_dir, roi_1_name, roi_2_name, filepath_func, filepath_mask1, filepath_mask2, results_save_dir, save_prediction)
    print("\naverage results across runs")
    avg_runs(model_type, sub, total_run, filepath_mask2, results_save_dir)
    print("\ndone!")

    log_filename = results_save_dir+sub+"_"+model_type+"_log.txt"
    log_file = open(log_filename, 'w')
    log_file.write("sub = " + sub + ",\n")
    log_file.write("model_type = " + model_type + ",\n")
    log_file.write("total_run = " + str(total_run) + ",\n")
    log_file.write("predictor_roi: " + roi_1_name + ",\n") 
    log_file.write("target_roi: " + roi_2_name + ". ")
    log_file.close()
