# 비디오 프레임을 이미지로 변환

import cv2
import os


print('[[ 비디오 -> 이미지 변환기 ]]')


video_list = os.listdir('inputvideo/')  # 비디오 저장 위치
print('비디오를 선택하세요')
for i in range(len(video_list)):  # 비디오 리스트 출력
    print('[' + str(i + 1) + ']', video_list[i])
user_select_video_num = int(input('숫자입력='))  # 변환할 비디오 선택하기
user_select_video_name = video_list[user_select_video_num-1]  # 선택한 비디오 이름 가져오기
print(user_select_video_name+'이 선택되었습니다.')


image_directory_path = 'outputimage/' + user_select_video_name[:-4]  # 이미지 저장용 폴더 경로 및 이름 지정
os.makedirs(image_directory_path)  # 이미지 저장용 폴더 만들기
try:
    capture = cv2.VideoCapture('inputvideo/' + user_select_video_name)  # OpenCV 비디오 읽어들이기
    total_video_frame = str(int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))  # 비디오 총 프레임
    while True:
        ret, image = capture.read()
        now_video_frame = str(int(capture.get(cv2.CAP_PROP_POS_FRAMES)))  # 현재 작업중인 비디오 프레임
        cv2.imwrite(image_directory_path + "/" + now_video_frame + ".jpg", image)  # 이미지 출력
        print('진행중:[' + now_video_frame + '/' + total_video_frame + ']')

except KeyboardInterrupt:
    print('KeyboardInterrupt. USER STOPPED')

except:
    print('DONE!')

os.system('pause')