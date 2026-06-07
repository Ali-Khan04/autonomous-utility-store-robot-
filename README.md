# Autonomous Utility Store Robot — FYP

ROS 2 project for an autonomous mobile robot that navigates a utility store,
identifies products, and picks items using a servo arm.

**Status:** In Progress — Gazebo simulation phase

## Stack
- ROS 2 Humble
- Gazebo
- SLAM (slam_toolbox)
- Nav2
- RPLidar A1
- Ubuntu 22.04

## Package Structure
```
ros2_ws/
└── src/
    └── my_robot_pkg/
        ├── launch/      # Launch files
        ├── worlds/      # Gazebo world files
        ├── rviz/        # RViz2 config files
        ├── docs/        # Progress screenshots
        └── include/     # C++ headers (reserved)
```

## Progress

### Gazebo Simulation — LiDAR Visualization
![Gazebo LiDAR](src/my_robot_pkg/docs/gazebo_lidar.png)
TurtleBot3 loaded into custom store world. 360° LiDAR rays actively
detecting shelf obstacles in simulation.

### RViz2 — Live LiDAR from RPLidar A1
![RViz2 LiDAR](src/my_robot_pkg/docs/rviz2_lidar.png)
Real-time `/scan` data from the physical RPLidar A1 visualized in RViz2

### SLAM Mapping — Store Environment
![SLAM Map](src/my_robot_pkg/docs/slam.jpeg)
2D occupancy grid map generated using `slam_toolbox` inside the custom
store environment. The robot successfully performs real-time mapping and
localization using LiDAR data.


Real-time /scan data from physical RPLidar A1 hardware visualized in
RViz2. Confirms full sensor pipeline on Ubuntu + ROS 2.

### SLAM Mapping — Store Environment
![SLAM Map](src/my_robot_pkg/docs/slam.jpeg)

2D occupancy grid map generated using `slam_toolbox` inside the custom
store environment. The robot successfully performs real-time mapping and
localization using LiDAR data.

## Running the Simulation
```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
ros2 launch my_robot_pkg utility_store.launch.py
```

## Roadmap
- [x] Gazebo world setup
- [x] LiDAR sensor integration
- [x] SLAM mapping
- [ ] Nav2 autonomous navigation
- [ ] YOLOv8 product detection
- [ ] Servo arm control
- [ ] Full mission pipeline
