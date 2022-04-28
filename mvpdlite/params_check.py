from mvpdlite.custom_func import dimred_custom

def params_check(params):
    """
    Check the validity of parameters.
    """
    # check dimensionality reduction
    try:
       params.dim_reduction
    except AttributeError:
       print("Warning: you did not specify whether or not to use dimensionality reduction.")
       print("By default: no dimensionality reduction will be applied.\n")
       params.dim_reduction=False 
    
    if params.dim_reduction==True:
       try:
          params.dim_type
          if params.dim_type not in ['ica', 'pca']:
             print("Attempt to apply a custom dimensionality reduction method.")
             try:
                getattr(dimred_custom, params.dim_type)
             except AttributeError:
                print("Warning: fail to find the custom dimensionality reduction method.")
                print("By default: PCA will be applied.\n")
                params.dim_type='pca'
          try:
             params.num_dim
             if params.num_dim<=0:
                print("Warning: the number of dimensions after dimensionality reduction you specified is not valid.")
                print("By default: 3 dimensions will be used.\n")
                params.num_dim=3
          except AttributeError:
             print("Warning: you did not specify the number of dimensions after dimensionality reduction.")
             print("By default: 3 dimensions will be used.\n")
             params.num_dim=3
       except AttributeError:
          print("Warning: you did not specify a method to perform dimensionality reduction.")
          print("By default: PCA will be applied.\n")
          params.dim_type='pca'

    # check regularization term for linear regression
    try:
       params.lin_reg
    except AttributeError:
       print("Warning: you did not specify whether or not to add regularization to the linear regression model.")
       print("By default: no regularization will be added.\n")
       params.lin_reg=False

    if params.lin_reg==True: 
       try:
          params.reg_type
          if params.reg_type not in ['Ridge', 'Lasso', 'RidgeCV']:
             print("Warning: the regularization method you specified is not valid.")
             print("By default: Ridge regression (L2 regularization) will be applied.\n")
             params.reg_type='Ridge' 

          elif params.reg_type=='RidgeCV':
             try:
                params.reg_strength_list
             except AttributeError:
                print("Warning: For RidgeCV, you did not specify the array of regularization strength values to try.")
                print("By default: the values [0.001,0.01,0.1] will be tried.\n")
                params.reg_strength_list=[0.001,0.01,0.1] 
       except AttributeError:
          print("Warning: you did not specify the regularization method.")
          print("By default: Ridge regression (L2 regularization) will be applied.\n")
          params.reg_type='Ridge'

       try:
          params.reg_strength
       except AttributeError:
          print("Warning: you did not specify the regularization strength.")
          print("By default: the regularization strength 0.001 will be used.\n")
          params.reg_strength=0.001

    # check validity of leave k run out
    try:
       params.leave_k
       if params.leave_k<=0 or params.leave_k>=params.total_run:
          print("Warning: the leave-k-run-out you specified is not valid.")
          print("By default: leave-one-run-out cross-validation will be used.\n")
          params.leave_k=1
    except AttributeError:
       print("Warning: you did not specify the leave-k-run-out cross-validation.")
       print("By default: leave-one-run-out cross-validation will be used.\n")
       params.leave_k=1


