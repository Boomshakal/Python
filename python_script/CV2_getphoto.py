import cv2
import os


def getphoto():
    class_name = 'get_photo'
    photo_name = 1

    file = class_name + '/' + str(photo_name) + '.jpeg'
    print(file)
    if os.path.exists(file):
        print('1111')
        os.remove(file)
    else:
        os.mkdir(class_name)

    cap = cv2.VideoCapture(0)
    width = 640
    height = 480
    w = 360
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    crop_w_start = (width - w) // 2
    crop_h_start = (height - w) // 2

    # print(width, height)

    # get a frame
    ret, frame = cap.read()
    # show a frame
    frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]
    frame = cv2.flip(frame, 1, dst=None)
    cv2.imshow("capture", frame)

    # input = cv2.waitKey(1) & 0xFF

    cv2.imwrite("%s/%d.jpeg" % (class_name, photo_name),
                cv2.resize(frame, (480, 480), interpolation=cv2.INTER_AREA))
    # while True:
    #     # get a frame
    #     ret, frame = cap.read()
    #     # show a frame
    #     frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]
    #     frame = cv2.flip(frame, 1, dst=None)
    #     cv2.imshow("capture", frame)
    #
    #     input = cv2.waitKey(1) & 0xFF
    #
    #     if input == ord('z'):
    #         class_name = input("请输入存储目录：")
    #         while os.path.exists(class_name):
    #             class_name = input("目录已存在！请输入存储目录：")
    #         os.mkdir(class_name)
    #     elif input == ord('x'):
    #         cv2.imwrite("%s/%d.jpeg" % (class_name, index),
    #                     cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA))
    #         print("%s: %d 张图片" % (class_name, index))
    #         index += 1
    #     if input == ord('q'):
    #         break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    getphoto()
