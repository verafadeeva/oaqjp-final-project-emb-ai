import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        joy_output = emotion_detector("I am glad this happened")
        self.assertEqual(joy_output["dominant_emotion"], "joy")

        anger_output = emotion_detector("I am really mad about this")
        self.assertEqual(anger_output["dominant_emotion"], "anger")

        disgust_output = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_output["dominant_emotion"], "disgust")

        sadness_output = emotion_detector("I am so sad about this")
        self.assertEqual(sadness_output["dominant_emotion"], "sadness")

        fear_output = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_output["dominant_emotion"], "fear")



if __name__ == "__main__":
    unittest.main()