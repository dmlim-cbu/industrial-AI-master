#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int64.h"

#include <stdio.h> 
#include <stdlib.h> 
#include <time.h>

int main (int argc, char **argv)
{
    int iSecret, iGuess;

    ros::init(argc, argv, "rand_1d");
    ros::NodeHandle n;
    ros::Publisher rand_1d_pub = n.advertise<std_msgs::Int64>("rand1d", 1000);
   
    std_msgs::Int64 msg;

    srand (time(NULL));

    ros::Rate loop_rate(10);

    while (ros::ok())
    {       
        iSecret = rand() % 10 + 1;
        msg.data = iSecret; 

        ROS_INFO("Node(1) Random 1~10 : %d", msg.data);

        rand_1d_pub.publish(msg);

        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}
