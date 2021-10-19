#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int64.h"

int gNodeSum = 0;
int gNodeCnt = 0;

void chatterCallback(const std_msgs::Int64::ConstPtr& msg)
{
    gNodeSum = gNodeSum + msg->data;
    ROS_INFO("Node %d = %d", gNodeCnt+1, msg->data);
    gNodeCnt++;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "sum");
    ros::NodeHandle n;
    ros::Publisher sum_pub = n.advertise<std_msgs::Int64>("sum", 1000);

    ros::Subscriber sub_1 = n.subscribe("rand1d", 1000, chatterCallback);
    ros::Subscriber sub_2 = n.subscribe("rand2d", 1000, chatterCallback);
    
    std_msgs::Int64 msg;

    ros::Rate loop_rate(10);

    while (ros::ok())
    {               
        msg.data = gNodeSum; 
        sum_pub.publish(msg);

        if (gNodeCnt > 1) {
            ROS_INFO("Node(3) N1 + N2 = %d", gNodeSum);
            gNodeCnt = 0;
	    gNodeSum = 0;
        }

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}

