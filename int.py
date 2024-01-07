# import the necessary packages
from Main import main
main()
import sample_copy_2

def ocr(self):
    """
        Creates a process where frames are continuously grabbed from the exchange and processed by pytesseract OCR.
        Output data from pytesseract is stored in the self.boxes attribute.
        """
    while not self.stopped:
        if self.exchange is not None:  # Defends against an undefined VideoStream reference
            frame = self.exchange.frame

                # # # CUSTOM FRAME PRE-PROCESSING GOES HERE # # #
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                # frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
                # # # # # # # # # # # # # # # # # # # #

            frame = frame[self.crop_height:(self.height - self.crop_height),
                              self.crop_width:(self.width - self.crop_width)]

            self.boxes = pytesseract.image_to_data(frame, lang=self.language)

def put_ocr_boxes(boxes, frame, height, crop_width=0, crop_height=0):
    """
    Draws text bounding boxes at tesseract-specified text location. Also displays compatible (ascii) detected text
    Note: ONLY works with the output from tesseract image_to_data(); image_to_boxes() uses a different output format

    :param boxes: output tuple from tesseract image_to_data() containing text location and text string
    :param numpy.ndarray frame: CV2 display frame destination
    :param height: Frame height
    :param crop_width: (Default 0) Horizontal frame crop amount if OCR was performed on a cropped frame
    :param crop_height: (Default 0) Vertical frame crop amount if OCR was performed on a cropped frame
    :param view_mode: View mode to specify style of bounding box

    :return: CV2 frame with bounding boxes, and output text string for detected text
    """

    text = ''  # Initializing a string which will later be appended with the detected text
    if boxes is not None:  # Defends against empty data from tesseract image_to_data
        for i, box in enumerate(boxes.splitlines()):  # Next three lines turn data into a list
            box = box.split()
            if i != 0:
                if len(box) == 12:
                    x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
                    conf = box[10]
                    word = box[11]
                    x += crop_width  # If tesseract was performed on a cropped image we need to 'convert' to full frame
                    y += crop_height

                    conf_thresh, color = views(view_mode, int(float(conf)))

                    if int(float(conf)) > conf_thresh:
                        cv2.rectangle(frame, (x, y), (w + x, h + y), color, thickness=1)
                        text = text + ' ' + word

        if text.isascii():  # CV2 is only able to display ascii chars at the moment
            cv2.putText(frame, text, (5, height - 5), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 200, 200))

    return frame, text




