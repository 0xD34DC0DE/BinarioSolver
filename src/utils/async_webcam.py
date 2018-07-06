import threading
import cv2

# Code taken from https://github.com/gilbertfrancois/video-capture-async/blob/master/main/smbh/py/video/capture.py


class VideoCaptureAsync:
    def __init__(self, src=0, width=640, height=480):
        self.src = src
        self.cap = cv2.VideoCapture(self.src)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.grabbed, self.frame = self.cap.read()
        self.started = False
        self.read_lock = threading.Lock()
        self.window_name = "Webcam"
        self.window = None
        self.window_closed = True

    def set(self, var1, var2):
        self.cap.set(var1, var2)

    def start(self, window_name="Webcam"):
        if self.started:
            print('[!] Asynchronous video capture has already been started.')
            return None
        self.started = True
        self.window = cv2.namedWindow(window_name)
        self.window_name = window_name
        self.window_closed = False
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.start()
        return self

    def update(self):
        while self.started:
            grabbed, frame = self.cap.read()
            with self.read_lock:
                self.grabbed = grabbed
                self.frame = frame
                if not self.window_closed:
                    if cv2.getWindowProperty(self.window_name, 0) == -1:
                        self.window_closed = True
                    if not self.window_closed:
                        cv2.imshow(self.window_name, self.frame)

    def read(self):
        with self.read_lock:
            frame = self.frame.copy()
            grabbed = self.grabbed
        return grabbed, frame

    def is_closed(self):
        with self.read_lock:
            closed_status = self.window_closed
        return closed_status

    def stop(self):
        self.started = False
        if not self.window_closed:
            cv2.destroyWindow(self.window_name)
            self.window_closed = True
        self.window = None
        self.thread.join()

    def __exit__(self, exec_type, exc_value, traceback):
        self.cap.release()
