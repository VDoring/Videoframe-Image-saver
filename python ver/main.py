import cv2
import time
import os

vid_name = ''

def mainTitle():
    os.system('mode con cols=45 lines=10')
    os.system('title VFrame Image v0.1')
    print('Video Frame Image Converter')
    print('by VDoring\n\n')
    os.system('pause')


def fileNameSet():
    global vid_name

    os.system('cls')
    print('Input video file name.')
    vid_name = input('> ')


def convertFrameImage():
    global vid_name

    os.system('mode con cols=50 lines=10')
    os.system('title Converting..')

    try:
        capture = cv2.VideoCapture('inputVideo/%s.mp4'% vid_name)
        ret,image = capture.read()

        video_frame_all = capture.get(cv2.CAP_PROP_FRAME_COUNT)

        ret = True

        while ret:
            ret, image = capture.read()
            cv2.imwrite("outputImage/%d.jpg" %int(capture.get(cv2.CAP_PROP_POS_FRAMES)), image)
            print('Running.. [' + str(int(capture.get(cv2.CAP_PROP_POS_FRAMES))) + '/' + str(int(video_frame_all)) + ']')
        print('Done!')
        os.system('pause')
            
    except:
        print('ERR-Done!')
        os.system('pause')


# 메인코드
while True:
    mainTitle()
    fileNameSet()
    convertFrameImage()