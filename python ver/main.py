import cv2
import time
import os

# by VDoring. 2021-07-21
# 타이틀화면을 표시합니다.
def mainTitle():
    os.system('mode con cols=45 lines=10')
    os.system('title VFrame Image v0.2')
    print('\n       < Video Frame Image Converter >')
    print('            ver0.2 - by VDoring\n\n')
    os.system('pause')

# by VDoring. 2021-07-21
# inputVideo폴더 안에 있는 파일이름을 나열하고 사용자가 사용할 파일을 선택하게 합니다.
# 반환값: (파일이름).(확장자)
def fileNameSet():
    video_extension_list = ('.mp4', '.mov', '.avi') # 동영상 확장자 리스트

    while True:
        os.system('mode con cols=51 lines=40')
        print('                 < Input number >\n')

        vid_list = os.listdir('inputVideo/') # inputVideo 폴더에 저장되어있는 파일리스트 저장

        for i in range(len(vid_list)):
            print('['+str(i+1)+']', vid_list[i]) # inputVideo 폴더에 저장되어있는 파일리스트 출력

        try:
            vid_num = input('\n= ')

            if int(vid_num) <= 0:
                print('[!] Enter a right number! [!]')
                time.sleep(0.75)
                continue

            user_vid_name = vid_list[int(vid_num)-1] # 사용자가 선택한 파일 이름 저장

            for i in range(len(video_extension_list)):
                if os.path.isfile('inputVideo/' + user_vid_name[:-4] + video_extension_list[i]): # 만약 특정 확장자로 된 사용자가 선택한 파일을 찾을경우
                    return user_vid_name[:-4] + video_extension_list[i]

            print('[!] File not support! [!]')
            print('Support file: ',end='')
            for i in video_extension_list:
                print(i,end='')
            time.sleep(2)

        except KeyboardInterrupt:
            return 'EXIT'

        except:
            print('[!] Enter a right number! [!]')
            time.sleep(0.75)

# by VDoring. 2021-07-21
# 동영상 프레임을 추출하여 outputImage폴더에 사진으로 저장합니다.
def convertFrameImage(filename):
    os.system('mode con cols=25 lines=15')
    os.system('title Converting..')

    if filename == 'EXIT':
        return

    try:
        capture = cv2.VideoCapture('inputVideo/' + filename)
        
        video_frame_all = capture.get(cv2.CAP_PROP_FRAME_COUNT)

        while True:
            ret, image = capture.read()
            cv2.imwrite("outputImage/%d.jpg" %int(capture.get(cv2.CAP_PROP_POS_FRAMES)), image)
            print('Running.. [' + str(int(capture.get(cv2.CAP_PROP_POS_FRAMES))) + '/' + str(int(video_frame_all)) + ']')

    except KeyboardInterrupt:
        print('Stopped.')
        os.system('pause')
    
    except:
        print('Done!')
        os.system('pause')


# 메인코드 #
while True:
    mainTitle()
    convertFrameImage(fileNameSet())