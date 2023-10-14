from PIL import Image, ImageDraw
import torch


def draw_bounding_box(image: Image, results: torch.Tensor, id2label: dict) -> Image:
    draw = ImageDraw.Draw(image)
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        label = id2label[label.item()]
        draw.rectangle(box.tolist(), outline='red')
        draw.text((box[0], box[1]), label, fill='red', size=20)
    return image