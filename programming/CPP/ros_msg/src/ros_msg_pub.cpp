#include "ros/ros.h"
#include "ros_msg/mymsg.h"
#include <stdlib.h>
#include <iostream>
#include <vector>

std::vector<int> storedVector;

int main(int argc, char **argv)
{
    ros::init(argc, argv, "msg_pub");
    ros::NodeHandle n;
    ros::Publisher chatter_pub = n.advertise<ros_msg::mymsg>("ros_msg", 1);
    ros::Rate loop_rate(10);

    int count = 0;
    for(int i = 0;i<5;i++)
      storedVector.push_back(i);

    while (ros::ok())
    {
        ros_msg::mymsg pub_data;

        pub_data.header.frame_id = "/map";
        pub_data.header.seq = count;
        pub_data.header.stamp = ros::Time::now();

        pub_data.x = 20;
        pub_data.y = 30;

        storedVector.push_back(count*3);
        storedVector.erase(storedVector.begin());

        pub_data.testarray = storedVector;

        chatter_pub.publish(pub_data);
    
        std::cout << "test pub!" << std::endl;

        ros::spinOnce();
        loop_rate.sleep();
        ++count;
    }

    return 0;
}
