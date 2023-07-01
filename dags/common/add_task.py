from airflow.decorators import task, dag

@task
def sum_task(x, y):
    print(f"Task args: x={x}, y={y}")
    return x + y


@task
def task_no_virtualenv():
    # import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    import sys
    print("Python Version")
    print(sys.version)
    print("-----------")
    
    print("Init")
    x = np.arange(1, 25).reshape(12, 2)
    y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    print('Train:')
    print(x_train)
    print('Test:')
    print(x_test)
    print("Finished")


@task.virtualenv(
    task_id="virtualenv_python", requirements=["pandas==1.5.3", "numpy", "scikit-learn"], system_site_packages=False
)
def task_virtualenv():
    import numpy as np
    from sklearn.model_selection import train_test_split
    import sys
    print("Python Version")
    print(sys.version)
    print("-----------")
    
    print("Init")
    x = np.arange(1, 25).reshape(12, 2)
    y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    print('Train:')
    print(x_train)
    print('Test:')
    print(x_test)
    print("Finished")


@task.virtualenv(
    task_id="virtualenv_python2", 
    requirements=["pandas", "numpy", "scikit-learn"], 
    python_version="2",
    system_site_packages=False
)
def task_virtualenv_py2():

    import numpy as np
    from sklearn.model_selection import train_test_split
    import sys
    print("Python Version")
    print(sys.version)
    print("-----------")
    
    print("Init")
    x = np.arange(1, 25).reshape(12, 2)
    y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    print('Train:')
    print(x_train)
    print('Test:')
    print(x_test)
    print("Finished")

