from transformers import YolosForObjectDetection 
import torch
from PIL import Image
import requests
import io
import logging

from lib.plot import draw_bounding_box
from config import THRESHOLD_TO_SHOW_OBJECTS

def load_image_from_link(link: str) -> Image:
    response = requests.get(link)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        raise logging.ERROR("Failed to load image from link")


def detect_objects(
    image_link: str,
    model: YolosForObjectDetection,
    image_processor: YolosForObjectDetection
    ) -> torch.Tensor:
    image = load_image_from_link(image_link)
    processed_image = image_processor(image, return_tensors="pt")
    outputs = model(**processed_image)
    outputs_post_processed = image_processor.post_process_object_detection(
        outputs,
        threshold=THRESHOLD_TO_SHOW_OBJECTS,
        target_sizes=torch.tensor([image.size[::-1]])
        )[0]
    image_with_bbox = draw_bounding_box(image, outputs_post_processed, model.config.id2label)
    return image_with_bbox