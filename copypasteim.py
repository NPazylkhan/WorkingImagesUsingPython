from PIL import Image

im = Image.open("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\i.png")
imcopy = im.copy()
im2 = Image.open("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\im.png")
im2copy = im2.copy()

imcopy.paste(im2copy, (100, 200))

imcopy.save("C:\\Users\\Nurmakhan Pazylkhan\\source\\repos\\images\\imcopy.png")