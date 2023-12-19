#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/CameraInfo.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/opencv.hpp>
#include <cv_bridge/cv_bridge.h>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "camera_node");
  ros::NodeHandle nh;

  // 创建图像发布器
  ros::Publisher image_pub = nh.advertise<sensor_msgs::Image>("camera/image", 1);
  ros::Publisher camera_info_pub = nh.advertise<sensor_msgs::CameraInfo>("camera/camera_info", 1);

  // 打开摄像头
  cv::VideoCapture cap(0);
  if (!cap.isOpened())
  {
    ROS_ERROR("Failed to open the camera.");
    return -1;
  }

  // 设置摄像头参数
  cap.set(cv::CAP_PROP_FRAME_WIDTH, 640);
  cap.set(cv::CAP_PROP_FRAME_HEIGHT, 480);

  // 创建图像消息和相机信息消息
  sensor_msgs::ImagePtr img_msg;
  sensor_msgs::CameraInfo camera_info_msg;

  // 设置相机信息
  camera_info_msg.header.frame_id = "camera";
  camera_info_msg.height = 480;
  camera_info_msg.width = 640;
  // 其他相机参数设置...

  ros::Rate loop_rate(30);  // 设置循环频率为30Hz

  while (ros::ok())
  {
    cv::Mat frame;
    cap >> frame;  // 读取摄像头帧

    // 转换为ROS图像消息
    img_msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();

    // 发布图像消息和相机信息消息
    img_msg->header.stamp = ros::Time::now();
    image_pub.publish(img_msg);
    camera_info_pub.publish(camera_info_msg);

    ros::spinOnce();
    loop_rate.sleep();
  }

  // 关闭摄像头
  cap.release();

  return 0;
}