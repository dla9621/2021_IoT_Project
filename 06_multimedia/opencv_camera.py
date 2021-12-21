import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourcc(four charactercode)
# DIVX(avi), MP4V(mp4), X264(h264)
# fourcc = cv2.VideoWriter_fourcc(*'DIVX') # ('D', 'I', 'V', 'X')

# out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

# 사진 촬영하기
# ret, frame = cap.read()
# cv2.imshow('frame', frame)
# cv2.imwrite('output.jpg', frame)
# cv2.waitKey(0)

# 동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('frame', frame)
    # out.write(frame)

    # 1000 -> 1초, 10 -> 0.01초
    if cv2.waitKey(10) == 13:
        break

# 사용자 자원 해제
cap.release()
# out.release()
cv2.destroyAllWindows()