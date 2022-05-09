import os, sys
import pickle
from datetime import datetime
from mvpdlite.params_check import params_check
from mvpdlite.MVPD_lin_reg import run_lin_reg
from mvpdlite.avgrun_regression import avg_runs

def MVPD_exec(inputinfo, params):
    """
    Execute the selected MVPD model and average analysis across runs.

    INPUT FORMAT
    inputinfo - model input info structure
       inputinfo.sub - subject/participant whose data are to be analyzed
       inputinfo.filepath_func - the list of paths to the directories containing processed functional data
       inputinfo.results_save_dir - the path to the directory where the results will be saved

    params - model parameters structure
       params.mode_class - the general class of MVPD model to be used

    OUTPUT FORMAT
    logfile - TIMESTAMP_log.txt
    inputinfo+params variables - TIMESTAMP_variables.pkl
    """
    # create output folder if not exists
    if not os.path.exists(inputinfo.results_save_dir):
           os.mkdir(inputinfo.results_save_dir)

    total_run = len(inputinfo.filepath_func)
    params.total_run = total_run
    # check validity of parameters
    params_check(params)

    print("start running MVPD linear regression model for", inputinfo.sub)
    run_lin_reg(inputinfo, params) 
    print("\naverage results across runs")
    avg_runs(inputinfo, params)  
    print("\ndone!")

    # logging
    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    print(date)
    print("inputinfo:", vars(inputinfo))
    print("params:", vars(params))
    print("log information is saved in "+inputinfo.results_save_dir+date+"_log.txt")
    log_filename = inputinfo.results_save_dir+date+"_log.txt"
    log_file = open(log_filename, 'w')
    log_file.write("PyMVPD_LITE: version 0.0.4\n")
    log_file.write("input info:\n")
    log_file.write(str(vars(inputinfo)))
    log_file.write("model params:\n")
    log_file.write(str(vars(params))) 
    log_file.close()

    # store inputinfo & params as pickle for replication
    pickle.dump((vars(inputinfo), vars(params)), open(inputinfo.results_save_dir+date+"_variables.pkl", "wb"))

