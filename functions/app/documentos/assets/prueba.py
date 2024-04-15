# from pptx import Presentation
# from google.cloud import storage
# from pptx.enum.shapes import MSO_SHAPE_TYPE
# from io import BytesIO
# from os import getenv
# # from dotenv import load_dotenv
# import os  # Import the os module to work with file paths
# # import requests
# # load_dotenv()

# """Downloads a blob into memory."""
# # The ID of your GCS bucket
# bucket_name = getenv("BUCKET_NAME")

# # The ID of your GCS object
# blob_name = "Actividad2PresentaciónPruebasU.pptx"

# storage_client = storage.Client(project = getenv("GOOGLE_PROJECT_ID"))

# bucket = storage_client.bucket(bucket_name)

# # Construct a client side representation of a blob.
# # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
# # any content from Google Cloud Storage. As we don't need additional data,
# # using `Bucket.blob` is preferred here.
# blob = bucket.blob(blob_name)
# contents = blob.download_as_bytes()

# # print(
# #     "Downloaded storage object {} from bucket {} as the following bytes object: {}.".format(
# #         blob_name, bucket_name, contents.decode("utf-8")
# #     )
# # )

# prs = Presentation(BytesIO(contents))

# n = 0

# # Specify the directory where you want to save the images
# output_directory = "./functions/app/documentos/assets/"

# def write_image(shape):
#     global n
#     image = shape.image
#     # ---get image "file" contents---
#     image_bytes = image.blob
#     # ---make up a name for the file, e.g. 'image.jpg'---
#     image_filename = 'image{:03d}.{}'.format(n, image.ext)
#     # Specify the full path to save the image
#     image_path = os.path.join(output_directory, image_filename)
#     n += 1
#     print(image_path)
#     with open(image_path, 'wb') as f:
#         f.write(image_bytes)

# def visitor(shape):
#     if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
#         for s in shape.shapes:
#             visitor(s)
#     if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
#         write_image(shape)

# def iter_picture_shapes(prs):
#     for slide in prs.slides:
#         for shape in slide.shapes:
#             visitor(shape)

# iter_picture_shapes(prs)

# # text_runs will be populated with a list of strings,
# # one for each text run in presentation
# text_runs = ""

# for slide in prs.slides:
#     for shape in slide.shapes:
#         if not shape.has_text_frame:
#             continue
#         for paragraph in shape.text_frame.paragraphs:
#             for run in paragraph.runs:
#                 text_runs += run.text
#             text_runs += "\n"

# print(text_runs)