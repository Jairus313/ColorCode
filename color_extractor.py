from collections import Counter
from sklearn.cluster import KMeans
import cv2


class ColorCodes:
    def __init__(self, image_path=None, num_of_cluster=5):
        self.image_path = image_path
        self.num_of_cluster = num_of_cluster

    def preprocess(self, raw):
        image = cv2.resize(raw, (720, 480), interpolation = cv2.INTER_AREA)                                          
        image = image.reshape(image.shape[0]*image.shape[1], 3)

        return image

    def rgb_to_hex(self, rgb_color):
        hex_color = "#"

        for i in rgb_color:
            hex_color += ("{:02x}".format(int(i)))

        return hex_color

    def analyze(self, img):
        clf = KMeans(n_clusters = self.num_of_cluster)
        color_labels = clf.fit_predict(img)
        center_colors = clf.cluster_centers_
        counts = Counter(color_labels)
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [self.rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

        return hex_colors

    def get_rgb(self, hex_colors):
        color_codes = []

        for code in hex_colors:
            temp_dict = {}

            temp_dict["hex_code"] = code
            temp_dict["rgb_code"] = "rgb{}".format(tuple(int(code.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)))

            color_codes.append(temp_dict)

        return color_codes

    def extract_colors_code(self):
        try:
            image = cv2.imread(self.image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            modified_image = self.preprocess(image)
            color_code = self.analyze(modified_image)
            color_code = self.get_rgb(color_code)

            return color_code

        except Exception as e:
            print("Error occured {}".format(e))
            return False
    