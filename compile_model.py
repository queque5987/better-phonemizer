import torch
import os

def save_model_split():
    loaded = torch.load("pytorch_model.bin")
    for i, l in enumerate(loaded):
        # print("{}".format(l))
        tensor = loaded[l]
        # print()
        torch.save(tensor, 'model_splited/{}'.format(l))

def load_model_split():
    temp = []
    pytorch_model = []
    path = "model_splited"
    for m in os.listdir(path):
        # print("{}".format(m))
        loaded = torch.load(path + "/" + m)
        # print(loaded)
        temp = [m, loaded]
        pytorch_model.append(temp)
        temp = []
    print("state_dict loading completed")
    return dict(pytorch_model)

def dict_clean():
    temp = []
    pytorch_model = []
    path = "model_splited"
    for m in os.listdir(path):
        # print("{}".format(m))
        # loaded = torch.load(path + "/" + m)
        temp = [m, torch.tensor(0)]
        pytorch_model.append(temp)
        temp = []
    torch.save(dict(pytorch_model), "model_splited/pytorch_model.bin")

# if __name__ == "__main__":
    # loaded = torch.load("model\pytorch_model.bin")
    # for i, l in enumerate(loaded):
    #     print("{} tensor saved".format(l))
    #     tensor = loaded[l]
    #     torch.save(tensor, 'model_splited/{}.{}.pt'.format(i, l))
    # temp = []
    # pytorch_model = []
    # print(os.listdir("model_splited"))
    # path = "model_splited"
    # for m in os.listdir(path):
    #     print("loaded {} !!".format(m[3:-3]))
    #     # print(m[3:-3])
    #     loaded = torch.load(path + "/" + m)
    #     temp = [m[3:-3], loaded]
    #     pytorch_model.append(temp)
    #     temp = []
    # dict(pytorch_model)
    # dict_clean()