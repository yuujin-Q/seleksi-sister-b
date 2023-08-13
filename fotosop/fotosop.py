import time
import multiprocessing
from multiprocessing import Array, Queue
import numpy as np
from PIL import Image
import colorsys


def grayscale_filter(r, g, b):
    grayscale_value = int((int(r) + int(g) + int(b)) / 3)  # Convert to grayscale
    return (grayscale_value, grayscale_value, grayscale_value)    


def contrast_filter(r, g, b, c):
    contrast_func = lambda c, v : max(0, min(255, int(c) * (int(v) - 128) + 128))
    pixel_value = (contrast_func(c, r), contrast_func(c, g), contrast_func(c, b))
    return pixel_value


def saturation_filter(r, g, b, c):
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    s1 = max(0, min(1, c * float(s)))
    r1, g1, b1 = colorsys.hls_to_rgb(h, l, s1)
    pixel_value = (r1 * 255, g1 * 255, b1 * 255)
    return pixel_value


def image_filter(part_start, part_end, image_array, result_queue, filter_mode, args=None):
    for i in range(part_start, part_end):
        for j in range(image_array.shape[1]):
            r, g, b = image_array[i, j]
            pixel_value = (r, g, b)

            if filter_mode == 1:    # grayscale
                pixel_value = grayscale_filter(r, g, b)
            elif filter_mode == 2:  # contrast
                pixel_value = contrast_filter(r, g, b, args)
            elif filter_mode == 3:  # saturation
                pixel_value = saturation_filter(r, g, b, args)

            result_queue.put((i, j, pixel_value))


def main():
    # # INPUT # #
    valid_image = False
    while not valid_image:
        image_path = input("Input image path: ")
        try:
            image = Image.open(image_path)
            valid_image = True
        except FileNotFoundError:
            print("Enter a valid image path.")


    print("Filtering Mode:\n" +
          "1. RGB to Grayscale\n" +
          "2. Contrast\n" +
          "3. Saturation\n")

    filter_mode = 0
    while filter_mode < 1 or filter_mode > 3:
        filter_mode = int(input("Choice: "))
        if filter_mode < 1 or filter_mode > 3:
            print("Invalid filtering choice")

    extra_args = None
    if filter_mode == 2:
        extra_args = float(input("Input contrast value: "))
    if filter_mode == 3:
        extra_args = float(input("Input saturation multiplier value: "))
    

    # # MULTIPROCESSING # #
    num_processes = multiprocessing.cpu_count()  # Get the number of available CPU cores
    num_processes = 8

    image_array = np.array(image)  # Convert the PIL Image to a NumPy array
    result_array = np.zeros_like(image_array)  # Create an empty array to store resulting image
    result_queue = Queue()

    rows_per_process = image_array.shape[0] // num_processes
    processes = []

    time_start = time.time()
    for i in range(num_processes):
        part_start = i * rows_per_process
        part_end = min((i + 1) * rows_per_process, image_array.shape[0])

        process = multiprocessing.Process(
            target=image_filter,
            args=(part_start, part_end, image_array, result_queue, filter_mode, extra_args)
        )
        processes.append(process)
        process.start()

    for _ in processes:
        while not result_queue.empty():
            row, col, value = result_queue.get()
            result_array[row, col] = value

    for process in processes:
        process.join()

    time_end = time.time()
    time_diff = (time_end - time_start)
    print("Time: %s" % time_diff)


    result_image = Image.fromarray(result_array)
    result_image.show()
    result_image.save("%s-filter-%d.jpg" % (image_path, filter_mode))

    
if __name__ == '__main__':
    main()
