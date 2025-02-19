#include "ros/ros.h"
#include "ros_msg/mysrv.h"

bool add(ros_msg::mysrv::Request &req, ros_msg::mysrv::Response &res)
{
    res.sum = req.a + req.b;
    ROS_INFO("request: x=%ld, y=%ld", (long int)req.a,
    (long int)req.b);
    ROS_INFO("sending back response: [%ld]", (long int)res.sum);

    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "testsrv_server"/*"add_two_ints_server"*/);
    ros::NodeHandle n;
    ros::ServiceServer service = n.advertiseService("add_two_ints", add);
    ROS_INFO("Ready to add two ints.");

    ros::spin();

    return 0;
}

