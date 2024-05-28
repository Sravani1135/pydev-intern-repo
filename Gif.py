from PIL import Image
image_path_list=[r"C:\Users\V.SRAVANI\PycharmProjects\pythonProject1\hello\Gif_Creater\shinchan_images\Ashinchan.jpg",r"C:\Users\V.SRAVANI\PycharmProjects\pythonProject1\hello\Gif_Creater\shinchan_images\Bshinchan.jpg", r"C:\Users\V.SRAVANI\PycharmProjects\pythonProject1\hello\Gif_Creater\shinchan_images\Eshinchan.jpg"]
image_list=[Image.open(file)for file in image_path_list]
image_list[0].save(
    r"C:\Users\V.SRAVANI\PycharmProjects\pythonProject1\hello\Gif_Creater\output_Document.gif",
    save_all=True,
    append_images=image_list[1:],
    duration=400,
    loop=0

)