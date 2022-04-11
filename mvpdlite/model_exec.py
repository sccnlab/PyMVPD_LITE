import os, sys
from mvpdlite.params_check import params_check
from mvpdlite.MVPD_lin_reg import run_lin_reg
from mvpdlite.avgrun_regression import avg_runs

def MVPD_exec(inputinfo, params):
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
    print("inputinfo:", vars(inputinfo))
    print("params:", vars(params))
    print("log information is saved in "+inputinfo.results_save_dir+inputinfo.sub+"_log.txt")
    log_filename = inputinfo.results_save_dir+inputinfo.sub+"_log.txt"
    log_file = open(log_filename, 'w')
    log_file.write("input info:\n")
    log_file.write(str(vars(inputinfo)))
    log_file.write("model params:\n")
    log_file.write(str(vars(params))) 
    log_file.close()