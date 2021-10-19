#include "ros/ros.h"
#include <iostream>
#include <string>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "param_test");
    ros::NodeHandle n;
    double version;
    std::string name;
    bool paramBool;

    n.getParam("/version", version);
    n.getParam("/name", name);
    n.getParam("/param_bool", paramBool);

    ROS_INFO("version : %lf",version);
    ROS_INFO("name : %s",name.c_str());
    ROS_INFO("param_bool : %d",paramBool);
}
