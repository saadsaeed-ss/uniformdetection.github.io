import cv2
import numpy as np
from PIL import Image
from keras import models

model = models.load_model('new_model.h5')
video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()

    im = Image.fromarray(frame, 'RGB')

    im = im.resize((256, 256))
    img_array = np.array(im)

    img_array = np.expand_dims(img_array, axis=0)

    prediction = int(model.predict(img_array)[0][0])

    print(prediction)

    font = cv2.FONT_HERSHEY_SIMPLEX
    if prediction == 0:
        cv2.putText(frame,
                    'No uniform detected',
                    (20, 20),
                    font, 1,
                    (255, 0, 0),
                    2,
                    cv2.LINE_4)
    else:
        cv2.putText(frame,
                    'Uniform detected',
                    (20, 20),
                    font, 1,
                    (0, 128, 0),
                    2,
                    cv2.LINE_4)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
