import torch
#This command will return a boolean (True/False) letting you know if a GPU is available.
use_cuda = torch.cuda.is_available()
print(available_cuda)

# more detail about GPU
if available_cuda:
    print('__CUDNN VERSION:', torch.backends.cudnn.version())
    print('__Number CUDA Devices:', torch.cuda.device_count())
    print('__CUDA Device Name:',torch.cuda.get_device_name(0))
    print('__CUDA Device Total Memory [GB]:',torch.cuda.get_device_properties(0).total_memory/1e9)
