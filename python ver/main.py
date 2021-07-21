import cv2
import time
import os

vid_name = ''

# by VDoring. 2021-07-21
# 타이틀화면을 표시합니다.
def mainTitle():
    os.system('mode con cols=45 lines=10')
    os.system('title VFrame Image v0.1.1')
    print('\n       < Video Frame Image Converter >')
    print('            ver0.1.1 - by VDoring\n\n')
    os.system('pause')

# by VDoring. 2021-07-20
# 추출할 동영상 파일을 선택합니다.
def fileNameSet():
    global vid_name

    os.system('cls')
    print('Input video file name.')
    vid_name = input('> ')

# by VDoring. 2021-07-20
# 동영상 프레임을 추출하여 사진으로 저장합니다.
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

    except KeyboardInterrupt:
        print('Stopped!')
        os.system('pause')
    
    except:
        print('Done!')
        os.system('pause')


# 메인코드 #
while True:
    mainTitle()
    fileNameSet()
    convertFrameImage()