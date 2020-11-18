#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int64.h"

int gNodeAvg = 0;

void chatterCallback(const std_msgs::Int64::ConstPtr& msg)
{
    gNodeAvg = msg->data / 2;
    ROS_INFO("Node(4) Sum = %d, Average = %d",msg->data, gNodeAvg);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "avg");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("sum", 1000, chatterCallback);
    
    ros::spin();

    return 0;
}

