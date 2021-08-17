import cv2
import imutils
from OCR import get_letters, predict_letters


def show_img(let_list, img):
    green = (0, 255, 0)
    red = (255, 0, 0)
    for let in let_list:
        if let.rownum % 2 == 0:
            color = red
        else:
            color = green
        cv2.rectangle(img, (let.x, let.y), (let.x + let.w, let.y + let.h), color, 1)
        cv2.putText(img, str(let.prediction), (let.x, let.y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)

    cv2.imshow(f'letter', img)
    cv2.waitKey(0)


if '__main__' == __name__:

    img_path = 'images/mz1.jpg'
    image = cv2.imread(img_path)

    img_resized = imutils.resize(image, width=1200)

    letter_list = get_letters(image)
    letter_list = predict_letters(letter_list, image, cnn=True)

    show_img(letter_list, image)


