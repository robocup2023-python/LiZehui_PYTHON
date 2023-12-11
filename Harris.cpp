#include <iostream>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    Mat img = imread("lena.png", IMREAD_COLOR);
    if (!img.data)
    {
        cout << "请确定图像文件名是否正确" << endl;
        return -1;
    }
    // 转成灰度图像
    Mat gray;
    cvtColor(img, gray, COLOR_BGR2GRAY);

    // 计算Harris评价系数
    Mat harris;
    int blockSize = 2; // 邻域半径
    int apertureSize = 3;
    cornerHarris(gray, harris, blockSize, apertureSize, 0.04);

    // 归一化以便进行数据比较和结果显示
    Mat harrisn;
    normalize(harris, harrisn, 0, 255, NORM_MINMAX);
    // 将图像的数据类型变成CV_8U
    convertScaleAbs(harrisn, harrisn);

    // 寻找Harris角点
    vector<KeyPoint> KeyPoints;
    for (int row = 0; row < harrisn.rows; row++)
    {
        for (int col = 0; col < harrisn.cols; col++)
        {
            int R = harrisn.at<uchar>(row, col);
            if (R > 125)
            {
                // 将角点存入KeyPoint中
                KeyPoint KeyPoint;
                KeyPoint.pt.y = row;
                KeyPoint.pt.x = col;
                KeyPoints.push_back(KeyPoint);
            }
        }
    }
    // 绘制角点与显示结果
    drawKeypoints(img, KeyPoints, img);
    imshow("系数矩阵", harrisn);
    imshow("Harris角点", img);
    waitKey(0);
    return 0;
}