#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(){
    //Read image over which cca will be applied
    Mat image = imread("../assets/cca.png", IMREAD_GRAYSCALE);

    //Get binary image
    Mat binaryImage;
    threshold(image, binaryImage, 127, 255, THRESH_BINARY);

    //Get connected components
    Mat labelImage;
    connectedComponents(binaryImage, labelImage);

    //Get the clone of input image to work on so that we can compare input and output images finally
    Mat imLabelClone = labelImage.clone();

    //Find min and max pixel values and their location in the image
    Point minPos, maxPos;
    double min, max;
    minMaxLoc(imLabelClone, &min, &max, &minPos, &maxPos);

    //Normalize the image so that min values in 0 and max value is 255
    imLabelClone = 255 * (imLabelClone - min)/(max - min);

    //Convert image to 8 bits
    imLabelClone.convertTo(imLabelClone, CV_8U);

    //Apply color map to images
    applyColorMap(imLabelClone, imLabelClone, COLORMAP_JET);
    
    //Create windows to display images
    namedWindow("input image", WINDOW_NORMAL);
    namedWindow("cca image", WINDOW_NORMAL);

    //Display images
    imshow("input image", binaryImage);
    imshow("cca image", imLabelClone);
    
    //Press esc on keyboard to exit
    waitKey(0);

    //Close all the opened windows
    destroyAllWindows();

    return 0;
}