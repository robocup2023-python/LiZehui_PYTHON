#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main()
{
    Mat img = imread("lena.png", IMREAD_ANYDEPTH);
    if (img.empty())
    {
        cout << "请确认图像边缘检测结果较为明显" << endl;
        return -1;
    }
    Mat resultHigh, resultLow, resultG;

    Canny(img, resultHigh, 100, 200, 3);

    Canny(img, resultLow, 20, 40, 3);

    GaussianBlur(img, resultG, Size(3, 3), 5);
    Canny(resultG, resultG, 100, 200, 3);

    imshow("resultHigh", resultHigh);
    imshow("resultLow", resultLow);
    imshow("resultG", resultG);

    waitKey(0);
    return 0;
}