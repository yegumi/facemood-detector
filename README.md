This model classifies facial expresion into different basic mood.

The main goal I worked on this wasn't to build a production-ready model.

Mostly I wanted to work with image datasets, preprocessing them, and working with related ML tools like Tensorflow and OpenCV.

So I shall say that improving model confidence and high accuracy and recall weren't the primary goal of this project, but anyway precision, recall, accuracy and F1 (on their own definition) are in `explore_dataset.ipynb`.

But my main reason for this project was to see how I can link my model with DRF.

This project was really exciting to me cause as well as working with new packages I could see the complete process of taking data, changing its shape and training it and eventually use it inside a MVP.

Although I think this model isn't worth cloning but for anyone who is interested:

```bash
git clone https://github.com/yegumi/facemood-detector
cd facemood
pyhton -m venv venv
# activate venv based on the os and shell you are with
pip install -r requirements.txt
```

For webcam demo:

```bash
python webcam_face_detect.py
```

For UI interface (right now it only takes one image):

```bash
python manage.py runserver
```

and then open `facemood_frontend/test_page.html`
