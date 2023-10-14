from transformers import YolosForObjectDetection, YolosImageProcessor 
from config import MODEL_PATH


def load_model() -> YolosForObjectDetection:
    model = YolosForObjectDetection.from_pretrained(MODEL_PATH)
    return model

def load_image_processor() -> YolosImageProcessor:
    image_processor = YolosImageProcessor.from_pretrained(MODEL_PATH)
    return image_processor
    