import torch

if __name__ == '__main__':
    # pip install torch==2.0.0+cu117 torchvision==0.15.0+cu117 torchaudio==2.0.0+cu117 -f https://download.pytorch.org/whl/torch_stable.html
    print(torch.cuda.is_available())  # 应该返回 True
    print(torch.cuda.get_device_name(0))  # 应该返回 GPU 名称
