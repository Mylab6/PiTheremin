import time

import gluoncv as gcv
from gluoncv.utils import try_import_cv2
import mxnet as mx
# Load the model
net = gcv.model_zoo.get_model('ssd_512_mobilenet1.0_voc', pretrained=True)
# Compile the model for faster speed
net.hybridize()
# Load the webcam handler
cv2 = try_import_cv2()

cap = cv2.VideoCapture(0, cv2.CAP_V4L)
time.sleep(5) ### letting the camera autofocus

axes = None
NUM_FRAMES = 10 # you can change this
for i in range(NUM_FRAMES):
    # Load frame from the camera
    ret, frame = cap.read()

    # Image pre-processing
    frame = mx.nd.array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).astype('uint8')
    rgb_nd, frame = gcv.data.transforms.presets.ssd.transform_test(frame, short=512, max_size=700)

    # Run frame through network
    class_IDs, scores, bounding_boxes = net(rgb_nd)

    # Display the result
    img = gcv.utils.viz.cv_plot_bbox(frame, bounding_boxes[0], scores[0], class_IDs[0], class_names=net.classes)
    gcv.utils.viz.cv_plot_image(img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()