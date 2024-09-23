from PIL import Image
import os


def process_image(image_path, output_path):
    # 打开图片并转换为灰度图
    with Image.open(image_path) as img:
        img_gray = img.convert('L')  # 转换为灰度图

        # 创建一个新的图片，用于存放修改后的像素值
        new_img = Image.new('L', img_gray.size)

        # 遍历图片的每一个像素
        for x in range(img_gray.width):
            for y in range(img_gray.height):
                pixel = img_gray.getpixel((x, y))

                # 根据灰度值范围修改像素值
                if 0 <= pixel <= 25:
                    new_pixel = 0
                elif 26 <= pixel <= 134:
                    new_pixel = 85
                elif 135 <= pixel <= 209:
                    new_pixel = 170
                elif 210 <= pixel <= 255:
                    new_pixel = 255
                else:
                    new_pixel = pixel  # 理论上这个分支不会被执行

                # 设置新图片的像素值
                new_img.putpixel((x, y), new_pixel)

                # 保存修改后的图片
        new_img.save(output_path)


def process_folder(folder_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

        # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            process_image(input_path, output_path)

        # 指定输入和输出文件夹


input_folder = "D:\\PyCharmDataLifangu\\240918Proj_UNet_zoo\\data\\CMR_short\\train\\labels1"
output_folder = "D:\\PyCharmDataLifangu\\240918Proj_UNet_zoo\\data\\CMR_short\\train\\labels"

# 处理文件夹
process_folder(input_folder, output_folder)