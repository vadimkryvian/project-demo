from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun


#each pipe creates 20 jobs that runs one by one change the pipe number to select how much pipelines you want to run in parllel
#for example if you set pipe_num=3, it will run 3 pipelines in parller and each one of them will run 20 jobs and in total it will run 3*20=60 jobs

pipe_num = 3
def kfpipeline():
    with dsl.ParallelFor([i for i in range(pipe_num)]) as item:
        step_1 = mlrun.run_function('func')
        step_2 = mlrun.run_function('func').after(step_1)
        step_3 = mlrun.run_function('func').after(step_2)
        step_4 = mlrun.run_function('func').after(step_3)
        step_5 = mlrun.run_function('func').after(step_4)
        step_6 = mlrun.run_function('func').after(step_5)
        step_7 = mlrun.run_function('func').after(step_6)
        step_8 = mlrun.run_function('func').after(step_7)
        step_9 = mlrun.run_function('func').after(step_8)