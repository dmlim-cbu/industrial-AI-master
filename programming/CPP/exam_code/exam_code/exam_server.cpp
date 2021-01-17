#include "ros/ros.h"
#include "ros_msg/exam.h"
#include "ros_msg/circle_msg.h"

bool add(ros_msg::exam::Request &req, ros_msg::exam::Response &res)
{
    res.Area = req.radius * req.radius * 3.14;
    ROS_INFO("Server::request: radius=%ld", (long int)req.radius);
    ROS_INFO("Server::sending back response: [%ld]", (long int)res.Area);
    
    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "exam_server");
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("circle_area", add);
    ROS_INFO("Server::Circle area calc server.");
    
    ros::spin();

    return 0;
}

