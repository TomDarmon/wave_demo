from h2o_wave import ui
import base64
import PIL
from io import BytesIO

def get_header():
    header_ui = ui.header_card(
        box=ui.box(zone='header'),
        title='Object Detection Demo',
        subtitle='This is a demo of object detection using Hugging Face Transformers',
        )
    return header_ui



def get_meta_page():
    meta_page = ui.meta_card(box='', layouts=[
        ui.layout(
        breakpoint='xl',
        width='1200px',
        zones=[
            ui.zone('header'),
            ui.zone('body'),
            ui.zone('image'),
            ]
        ),
    ])
    return meta_page

def get_form():
    form_ui = ui.form_card(box=ui.box(zone='body'),
    items=[
        ui.textbox(name='link_input', label='Enter the URL of an image for object detection'),
        ui.button(name='submit', label='Submit', primary=True),
        ]
        )
    return form_ui

def get_image_card(image: PIL.Image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()
    image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    image_card = ui.image_card(
        box=ui.box(zone='image'),
        title='Detected Objects',
        path=f'data:image/png;base64,{image_b64}',
    )
    return image_card