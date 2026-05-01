import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node 

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')
    launch_file_dir = os.path.join(turtlebot3_gazebo, 'launch')
    pkg_dir = get_package_share_directory('my_robot_pkg')
    map_file = os.path.join(pkg_dir, 'maps', 'utility_store_map.yaml')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')


    world = os.path.join(
        pkg_dir,
        'worlds', 'utility_store.world'
    )

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    robot_state_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose
        }.items()
    )
    rviz_node = Node(
    package='rviz2',
    executable='rviz2',
    arguments=['-d', os.path.join(pkg_dir, 'rviz', 'utility_store.rviz')],
    parameters=[{'use_sim_time': use_sim_time}],
)
    map_server = Node(
    package='nav2_map_server',
    executable='map_server',
    name='map_server',
    output='screen',
    parameters=[{
        'yaml_filename': map_file,
        'use_sim_time': use_sim_time
    }]
)
    lifecycle_manager = Node(
    package='nav2_lifecycle_manager',
    executable='lifecycle_manager',
    name='lifecycle_manager_localization',
    output='screen',
    parameters=[{
        'use_sim_time': use_sim_time,
        'autostart': True,
        'node_names': ['map_server']
    }]
)

    ld = LaunchDescription()
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(robot_state_publisher_cmd)
    ld.add_action(spawn_turtlebot_cmd)
    ld.add_action(rviz_node)
    ld.add_action(map_server)
    ld.add_action(lifecycle_manager)

    return ld