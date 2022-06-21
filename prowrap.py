import cv2
import math
import numpy as np
import utils

def img_preprocess(input_dir):
    original_img = cv2.imread(input_dir)
    original_img=cv2.resize(original_img,(600,800), interpolation=cv2.INTER_CUBIC)
    gray_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_img, (9, 9), 0)                     # 高斯模糊去噪（设定卷积核大小影响效果）
    _, RedThresh = cv2.threshold(blurred, 165, 255, cv2.THRESH_BINARY)  # 设定阈值165（阈值影响开闭运算效果）
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))          # 定义矩形结构元素
    closed = cv2.morphologyEx(RedThresh, cv2.MORPH_CLOSE, kernel)       # 闭运算（链接块）
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)           # 开运算（去噪点）
    return original_img, gray_img, RedThresh, closed, opened

def findContours_biggest(original_img, opened):
    contours, hierarchy = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #c = sorted(contours, key=cv2.contourArea, reverse=True)[0]   # 计算最大轮廓的旋转包围盒
    #rect = cv2.minAreaRect(c)                                    # 获取包围盒（中心点，宽高，旋转角度）
    #box = np.int0(cv2.boxPoints(rect))                           # box
    #draw_img = cv2.drawContours(original_img.copy(), [box], -1, (0, 0, 255), 3)
    print(contours)
    return box, draw_img
def Perspective_transform(box,original_img):
    #orignal_w = math.ceil(np.sqrt((box[3][1] - box[2][1])**2 + (box[3][0] - box[2][0])**2))
    #orignal_h= math.ceil(np.sqrt((box[3][1] -  box[0][1])**2 + (box[3][0] - box[0][0])**2))
    size=original_img.shape;
    orignal_w = size[1]
    orignal_h=  size[0]

    #pts1 = np.float32(utils.reorder(box))

    pts1=np.float32([[88, 415],[]])
    pts2 = np.float32([[0,0], [orignal_w, 0], [0, orignal_h], [orignal_w, orignal_h]])

    print(box[0])
    print(pts1)
    print(pts2)
    # 生成透视变换矩阵；进行透视变换
    M = cv2.getPerspectiveTransform(pts1, pts2)
    result_img = cv2.warpPerspective(original_img, M, (int(orignal_w),int(orignal_h)))

    return result_img



if __name__=="__main__":
    input_dir = "14.jpg"
    original_img, gray_img, RedThresh, closed, opened = img_preprocess(input_dir)
    box, draw_img = findContours_biggest(original_img, RedThresh)
    result_imgnew = Perspective_transform(box, original_img)
    cv2.imshow("original", original_img)
    cv2.imshow("result_img", result_imgnew)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
