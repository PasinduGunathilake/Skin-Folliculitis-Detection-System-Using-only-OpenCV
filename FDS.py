import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'src\si.jpg')
img1 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img2 = cv.cvtColor(img1,cv.COLOR_RGB2HSV)
grayimg = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

print(img.shape)
print(grayimg.shape)
plt.imshow(grayimg,cmap = 'gray')

ret, thresh = cv.threshold(grayimg,100,255,cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#cv.drawContours(img, contours, 100, (0, 0, 255), 2)
print(len(contours))

folliculitis_count = 0

for cnt in contours:
    area = cv.contourArea(cnt)
    print(area)
    if(area >= 1.0 and area <= 410):
        #folliculitis_count = 1
        folliculitis_count = folliculitis_count +1
        cv.drawContours(img, [cnt], -1, (0, 0, 255), 1)
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255))
        cv.putText(img,f'{folliculitis_count}',(x+12,y+10),cv.FONT_HERSHEY_SIMPLEX,0.5,(36,255,8),2)
cv.rectangle(img,(5,375),(210,395),(36, 255, 12),2)       
cv.putText(img, f'Folliculitis Detected: {folliculitis_count}', (10, 390), cv.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

cv.imshow('LIVE',cv.resize(img,(800,600)))
cv.imshow('HSV',cv.resize(img2, (400, 300)))
#cv.imshow('GRAY',grayimg)
cv.imshow('THRESHOLD',cv.resize(thresh, (400, 300)))

cv.waitKey(0)
cv.destroyAllWindows()