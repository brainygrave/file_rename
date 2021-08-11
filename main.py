import os

path_way = os.getcwd()
images = os.listdir(path_way)
text_one = ""
text_two = ""

# OLD Text you want to change
answer_one = input("\nFIND TEXT: ").lower()
text_one = answer_one

# NEW Text you want to change
answer_two = input("\nCHANGE TEXT TO: ").lower()
text_two = answer_two

# Calling function to find and replace words in a directory
for images in images:
    os.rename(images, images.replace(text_one, text_two))


print("The changes are made")
