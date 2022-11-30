from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, max_iter

# Linked In
sc_width = 1128 * 4
sc_height = 191 * 4
shift_x = -1 + 0.020
shift_y = -0.310
scaler = 150

# sc_width = 600
# sc_height = 400
# shift_x = 0
# shift_y = 0
# scaler = 1


# Plot window
re_start = -(sc_width / sc_height)
re_end = sc_width / sc_height
im_start = -1
im_end = 1

re_start += shift_x * scaler
re_end += shift_x * scaler

im_start += shift_y * scaler
im_end += shift_y * scaler


palette = []

im = Image.new('RGB', (sc_width, sc_height), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, sc_width):
    for y in range(0, sc_height):
        # Pixel to number
        c = complex(re_start + (x / sc_width) * (re_end - re_start),
                    im_start + (y / sc_height) * (im_end - im_start))
        # get integration
        m = mandelbrot(c)

        # color calculations
        b = int(m % 256)
        g = int(m * 3 % 256)
        r = int(m * 9 % 256)

        color = int(m * 255 / max_iter)
        t_red = 150
        scaler = 255 / t_red
        if color < t_red:
            color *= scaler
        else:
            color = 255 - (color - t_red) * scaler
        color = int(color)

        # Plot the point
        draw.point([x, y], (color, 0, color))
        print(m)

im.save('output.png', 'PNG')
