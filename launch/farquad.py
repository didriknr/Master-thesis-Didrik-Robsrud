import os
import subprocess

def chmod():
    for i in range(4):
        os.system(f"sudo chmod 666 /dev/ttyACM{i}")
command0 = f"source {os.getcwd().rstrip('/src/Master-thesis-Didrik-Robsrud/launch')}/devel/setup.bash; roslaunch arnold.launch"
command1 = f"source /opt/ros/melodic/setup.bash; source /opt/ros/eloquent/setup.bash; ros2 launch tamago.py"
#command2 = f"source /opt/ros/eloquent/setup.bash; rqt"
#command3 = f"source /opt/ros/eloquent/setup.bash; rviz2"
chmod()


subprocess.run(["gnome-terminal", "--", "bash", "-c", command0])
subprocess.run(["gnome-terminal", "--", "bash", "-c", command1])
#subprocess.run(["gnome-terminal", "--", "bash", "-c", command2])



