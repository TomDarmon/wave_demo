from h2o_wave import main, app, Q
from lib.image_utils import detect_objects
from lib.model import load_model, load_image_processor

from lib.front import get_header, get_meta_page, get_form, get_image_card


@app('/demo')
async def serve(q: Q):
    if not q.client.initialized:
        q.client.initialized = True
        q.client.model = load_model()
        q.client.image_processor = load_image_processor()
        q.page['meta_page'] = get_meta_page()
        q.page['header'] = get_header()
        q.page['form'] = get_form()
        q.client.image_to_show = None
        
    if q.args.submit:
        q.client.image_to_show = detect_objects(
            image_link=q.args.link_input,
            model=q.client.model,
            image_processor=q.client.image_processor
        )

        q.page['image'] = get_image_card(q.client.image_to_show)

    await q.page.save()
