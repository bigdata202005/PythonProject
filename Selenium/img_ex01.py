from PIL import Image

# 이미지 열기
im = Image.open('python_main.png')

# 이미지 크기 출력
print(im.size)

# 이미지 이름을 변경하여 저장
im.save('python.png')

# Thumbnail 이미지 생성
size = (64, 64)
im.thumbnail(size)
im.save('python-thumb.png')

# 이미지의 일부분을 잘라서 저장
cropImage = im.crop((100, 100, 150, 150))
print(cropImage.size)
cropImage.save('python-crop.png')
