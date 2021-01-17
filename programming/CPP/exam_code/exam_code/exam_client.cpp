#include "ros/ros.h"
#include "ros_msg/exam.h"
#include "ros_msg/circle_msg.h"
#include <cstdlib>
#include <vector>

std::vector<int> radiusVector;
std::vector<int> areaVector;

int main(int argc, char **argv)
{
    ros::init(argc, argv, "exam_client");

    ros::NodeHandle n;
    ros::ServiceClient client = n.serviceClient<ros_msg::exam>("circle_area");
    ros::Publisher chatter_pub = n.advertise<ros_msg::circle_msg>("circle_msg", 1);
    ros_msg::exam srv; 
    ros_msg::circle_msg pub_data;

    int radius = 0, area = 0, count = 0;  

    while(ros::ok()) { 
        radius = rand() % 100;
        srv.request.radius = radius;

        ROS_INFO("Client::Circle radius: %ld", radius);

        if (client.call(srv))
        {
            ROS_INFO("Client::Circle area: %ld", (long int)srv.response.Area);
        }
        else
        {
            ROS_ERROR("Client::Failed to call service circle area !");
            return 1;
        }

        pub_data.header.seq = count;
        pub_data.header.stamp = ros::Time::now();

        radiusVector.push_back(radius);        
        pub_data.radius = radiusVector;

        areaVector.push_back(srv.response.Area);
        pub_data.area = areaVector;
        
        chatter_pub.publish(pub_data);

        count++;
        sleep(1);
    }

    return 0;
}

