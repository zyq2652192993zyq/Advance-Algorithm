> # Model save and load

参考资料：

* [pytorch加载保存查看checkpoint文件](https://blog.csdn.net/joyce_peng/article/details/104133594)

## PyTorch

### 保存加载checkpoint文件

```python
# 方式一：保存加载整个state_dict（推荐）
# 保存
torch.save(model.state_dict(), PATH)
# 加载
model.load_state_dict(torch.load(PATH))
# 测试时不启用 BatchNormalization 和 Dropout
model.eval()
```

```python
# 方式二：保存加载整个模型
# 保存
torch.save(model, PATH)
# 加载
model = torch.load(PATH)
model.eval()
```

### 跨GPU和CPU

```python
# GPU上保存，CPU上加载
# 保存
torch.save(model.state_dict(), PATH)
# 加载
device = torch.device('cpu')
model.load_state_dict(torch.load(PATH, map_location=device))
# 如果是多gpu保存，需要去除关键字中的module，见第4部分
```

```python
# GPU上保存，GPU上加载
# 保存
torch.save(model.state_dict(), PATH)
# 加载
device = torch.device("cuda")
model.load_state_dict(torch.load(PATH))
model.to(device)
```

```python
# CPU上保存，GPU上加载
# 保存
torch.save(model.state_dict(), PATH)
# 加载
device = torch.device("cuda")
# 选择希望使用的GPU
model.load_state_dict(torch.load(PATH, map_location="cuda:0"))  
model.to(device)
```

### 查看checkpoint文件内容

```python
# 打印模型的 state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())
```

