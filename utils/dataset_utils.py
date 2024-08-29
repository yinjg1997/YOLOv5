import os
import shutil
import random


def split_dataset(src_dir, dataset_name, val_ratio=0.2):
    """
    将数据集划分为训练集和验证集，并按指定目录结构保存

    参数:
    - src_dir: 原始数据的目录
    - dataset_name: 数据集名称，将用于目标目录结构
    - val_ratio: 验证集所占比例，默认为0.2
    """
    # 创建目标目录结构
    dest_dir = '../datasets'
    images_train_dest = os.path.join(dest_dir, dataset_name, 'images', 'train')
    images_val_dest = os.path.join(dest_dir, dataset_name, 'images', 'val')
    labels_train_dest = os.path.join(dest_dir, dataset_name, 'labels', 'train')
    labels_val_dest = os.path.join(dest_dir, dataset_name, 'labels', 'val')

    os.makedirs(images_train_dest, exist_ok=True)
    os.makedirs(images_val_dest, exist_ok=True)
    os.makedirs(labels_train_dest, exist_ok=True)
    os.makedirs(labels_val_dest, exist_ok=True)

    # 获取所有图片文件和标签文件
    images_train_src = os.path.join(src_dir, 'images')
    labels_train_src = os.path.join(src_dir, 'labels')

    # 常见图片格式
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')

    image_files = [f for f in os.listdir(images_train_src) if f.lower().endswith(image_extensions)]
    label_files = [f for f in os.listdir(labels_train_src) if f.endswith('.txt')]

    # 调试信息：打印文件列表
    print("图片文件列表:", image_files)
    print("标签文件列表:", label_files)

    # 确保图片文件和标签文件数量一致
    assert len(image_files) == len(label_files), "图片文件和标签文件数量不一致"

    # 检查文件名是否匹配
    image_files_set = {os.path.splitext(f)[0] for f in image_files}
    label_files_set = {os.path.splitext(f)[0] for f in label_files}
    assert image_files_set == label_files_set, "图片文件和标签文件名不匹配"

    # 随机打乱文件列表
    combined = list(zip(image_files, label_files))
    random.shuffle(combined)
    image_files[:], label_files[:] = zip(*combined)

    # 计算验证集大小
    val_size = int(len(image_files) * val_ratio)

    # 划分训练集和验证集
    val_image_files = image_files[:val_size]
    train_image_files = image_files[val_size:]

    val_label_files = label_files[:val_size]
    train_label_files = label_files[val_size:]

    # 复制文件到目标目录
    for img_file, lbl_file in zip(train_image_files, train_label_files):
        shutil.copy(os.path.join(images_train_src, img_file), os.path.join(images_train_dest, img_file))
        shutil.copy(os.path.join(labels_train_src, lbl_file), os.path.join(labels_train_dest, lbl_file))

    for img_file, lbl_file in zip(val_image_files, val_label_files):
        shutil.copy(os.path.join(images_train_src, img_file), os.path.join(images_val_dest, img_file))
        shutil.copy(os.path.join(labels_train_src, lbl_file), os.path.join(labels_val_dest, lbl_file))

    print("数据集划分完成！")


if __name__ == '__main__':
    # 示例调用
    split_dataset(r'C:\Users\he3\Downloads\Peace.v12i.yolov5pytorch\train', 'pubg')
