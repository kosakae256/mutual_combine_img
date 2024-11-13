import cv2
import numpy as np

# 画像を読み込みます
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# 二つの画像のサイズを確認し、大きい方に合わせてトリミングします
height = max(image1.shape[0], image2.shape[0])
width = max(image1.shape[1], image2.shape[1])

# 画像のサイズを大きい方に合わせてトリミングまたはリサイズします
image1_resized = cv2.resize(image1, (width, height))
image2_resized = cv2.resize(image2, (width, height))

# 交互にピクセルを配置するための空の画像を作成します
result = np.zeros_like(image1_resized)

# ピクセルを交互に配置
for i in range(height):
    for j in range(width):
        if (i + j) % 2 == 0:
            result[i, j] = image1_resized[i, j]  # 画像1のピクセル
        else:
            result[i, j] = image2_resized[i, j]  # 画像2のピクセル

# 結果の画像を保存します
cv2.imwrite('combined_image.jpg', result)