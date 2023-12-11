#include "opencv2/opencv.hpp"
#include <iostream>
using namespace std;
using namespace cv;
int main()
{
    // 读取图像,黑白图像边缘检测结果较为明显
    Mat img = imread("lena.png", IMREAD_ANYCOLOR);
    if (img.empty())
    {
        cout << "请确定图像文件名是否正确" << endl;
        return -1;
    }
    Mat resultX, resultY, resultXY;
    // X方向一阶边缘
    Sobel(img, resultX, CV_16S, 2, 0, 1);
    convertScaleAbs(resultX, resultX);
    // Y方向一阶边缘
    Sobel(img, resultY, CV_16S, 0, 1, 3);
    convertScaleAbs(resultY, resultY);
    // 整幅图像的一阶边缘
    resultXY = resultX + resultY;
    // 保存为9级压缩的png图像
    // vector<int> compression_params;
    // compression_params.push_back(IMWRITE_PNG_COMPRESSION);
    // compression_params.push_back(9);
    // 显示并保存图像
    imshow("resultX", resultX);
    // imwrite("resultX.png", resultX, compression_params);
    imshow("resultY", resultY);
    // imwrite("resultY.png", resultY, compression_params);
    imshow("resultXY", resultXY);
    // imwrite("resultXY.png", resultXY, compression_params);
    waitKey(0);
    return 0;
}