import re
import os
import sys
from tqdm import tqdm
import random
import torch
import torch.nn.functional as F
from colorama import Fore, Style, init

init(autoreset=True)

args = sys.argv
words = open(args[1], "r", encoding="utf-8").read().splitlines()


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def build_vocabulary(words):
    chars = sorted(list(set("".join(words))))
    stoi = {s: i + 1 for i, s in enumerate(chars)}
    stoi["."] = 0
    itos = {i: s for s, i in stoi.items()}
    print(itos)
    return words, stoi, itos


block_size = 3


def build_dataset(words, stoi):
    X, Y = [], []
    for w in words:
        context = [0] * block_size
        for ch in w + ".":
            ix = stoi[ch]
            X.append(context)
            Y.append(ix)
            context = context[1:] + [ix]

    X = torch.tensor(X)
    Y = torch.tensor(Y)
    print(X.shape, Y.shape)
    return X, Y


words, stoi, itos = build_vocabulary(words)
build_dataset(words, stoi)

random.seed(42)
random.shuffle(words)
n1 = int(0.8 * len(words))
n2 = int(0.9 * len(words))

torch.save(stoi, "stoi.pth")
print(Fore.GREEN + Style.BRIGHT + "создан файл stoi.pth")

Xtr, Ytr = build_dataset(words[:n1], stoi)
Xdev, Ydev = build_dataset(words[n1:n2], stoi)
Xte, Yte = build_dataset(words[n2:], stoi)

g = torch.Generator().manual_seed(42)
C = torch.randn((len(itos), 10), generator=g)
W1 = torch.randn((30, 50), generator=g)
b1 = torch.randn(50, generator=g)
W2 = torch.randn((50, len(itos)), generator=g)
b2 = torch.randn(len(itos), generator=g)
parameters = [C, W1, b1, W2, b2]

print(sum(p.nelement() for p in parameters))

for p in parameters:
    p.requires_grad = True

lre = torch.linspace(-3, 0, 1000)
lrs = 10**lre

lri = []
lossi = []
stepi = []

cls()

for i in tqdm(range(20000), desc="Traning process:"):

    # minibatch construct
    ix = torch.randint(0, Xtr.shape[0], (32,))

    # forward pass
    emb = C[Xtr[ix]]
    h = torch.tanh(emb.view(-1, 30) @ W1 + b1)
    logits = h @ W2 + b2
    loss = F.cross_entropy(logits, Ytr[ix])
    # print(loss.item())

    # backward pass
    for p in parameters:
        p.grad = None
    loss.backward()

    lr = 0.1 if i < 100000 else 0.01
    for p in parameters:
        p.data += -lr * p.grad

    stepi.append(i)
    lossi.append(loss.log10().item())

emb = C[Xtr]
h = torch.tanh(emb.view(-1, 30) @ W1 + b1)
logits = h @ W2 + b2
loss = F.cross_entropy(logits, Ytr)
print(Style.BRIGHT + f"train loss: {loss.item():.2f}")

torch.save({"C": C, "W1": W1, "b1": b1, "W2": W2, "b2": b2}, "model.pth")
print(Fore.GREEN + Style.BRIGHT + "создан файл model.pth")