import torch

# Create a random tensor
x = torch.rand(5, 3)
print("Tensor:")
print(x)

# Check CUDA (GPU) support
print(f"CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"Device Name: {torch.cuda.get_device_name(0)}")