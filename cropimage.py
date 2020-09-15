from PIL import Image

im = Image.open("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\i.png")

cp = im.crop((130, 120, 200, 200))

cp.show()