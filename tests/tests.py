import unittest
import cv2
import numpy as np

from image_translation.to_ascii import ASCIIConverter


class TestToASCII(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_build_ascii(self):
        converter = ASCIIConverter()

        indices = np.array([[0, 1, 2], [3, 4, 5]])

        ascii_art = converter.build_ascii(indices)
        print(ascii_art)

        with open("test_build_ascii.txt", 'r') as file:
            true_answer = file.read()
            print(true_answer)

        self.assertEqual(ascii_art, true_answer)

    def test_convert_img_to_ascii(self):
        converter = ASCIIConverter()

        img = cv2.imread("ex1.png", 1)
        ascii_art = converter.convert_img_to_ascii(img)

        with open("ex1.txt", 'r') as file:
            ex1_ascii = file.read()

        self.assertEqual(ascii_art, ex1_ascii)

        img = cv2.imread("ex2.jpg", 1)
        ascii_art = converter.convert_img_to_ascii(img)

        with open("ex2.txt", 'r') as file:
            ex2_ascii = file.read()

        self.assertEqual(ascii_art, ex2_ascii)
