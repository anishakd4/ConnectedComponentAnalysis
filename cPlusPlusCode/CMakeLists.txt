cmake_minimum_required(VERSION 2.8.12)


PROJECT(anishFaceLandmarkDetector)


######################## EDIT IF REQUIRED ####################
# ### If CMake is not able to find the path to OpenCV installation then Uncomment the line below and specify the path to OpenCV directory 
##(i.e. the path to the OpenCVConfig.cmake file). Check the examples given below. 
#SET(OpenCV_DIR Enter-the-path-of-OpenCV-installation-on-your-system)


################### OpenCV_DIR Examples  #####################

### MACOS : /usr/local/Cellar/opencv/3.3.1_1/share/OpenCV/

### UBUNTU : /usr/local/share/OpenCV/

### WINDOWS : C:\Users\yourname\Documents\opencv-3.3.1\build\install

##############################################################


###################   ***DO NOT EDIT***  #####################

#############  Common Instructions for all Users  ############
find_package( OpenCV REQUIRED )

include_directories( ${OpenCV_INCLUDE_DIRS})

MACRO(add_anish_executable name)
  ADD_EXECUTABLE(${name} ${name}.cpp)
  TARGET_LINK_LIBRARIES(${name} ${OpenCV_LIBS})
ENDMACRO()

add_anish_executable(cca)