# RT1_final_assignment

### How to run the code
We should open three different prompts, beside the one where we run "roscore". In the first one we lunch the simulator by executing the command:
```
roslaunch final_assignment move_base.launch
```
In the second and in the third window we can run the two nodes by executing:
```
rosrun final_assignment user_interface.py
```
 and
 
...
rosrun final_assignment robot_control.py
...

While the code is running, at the moment of the choice 2 ( Choosing a target), we need to open a new shell to insert the target "manually". With this purpose we need to run:

...
rosrun final_assignment input_targeteserver.py
...


### Description of the content


