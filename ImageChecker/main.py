import cv2
import turtle as t
import time

Image_Path = r"images.webp" #Путь к файлу/ File Path

t.pensize(2)
t.right(90)
t.colormode(255)
t.speed(0)


img = cv2.imread(Image_Path)
cv2.imshow("Image", img)
print("Нажмите любую клавишу/ Press any key")
cv2.waitKey(0)
cv2.destroyAllWindows()
y, x = 0, 0
height, width, channels = img.shape
pixel = img[y, x]

print(f"Высота: {height} пикселей / Height is {height} pixel")
print(f"Ширина: {width} пикселей / Width is {width} pixel")
print(f"Количество каналов: {channels} / Count of channels is {channels}")
print(pixel, type(pixel))

for i in range(height):
    for a in range(width):
        CuP = img[i, a]
        CuP[[0, 2]] = CuP[[2, 0]]
        t.pencolor(CuP)
        t.penup()
        t.goto(a + 2, i + 2 - i * 2)
        t.pendown()
        t.forward(1)
        t.backward(1)

print("Картинка срисованна! / Work complete!")
t.mainloop()
