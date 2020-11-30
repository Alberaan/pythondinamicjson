#!python
# -*- coding: utf-8 -*-

import json
from types import SimpleNamespace

with open('data2.txt', 'r') as f:
    data = json.load(f)

x = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
print(x.Atributos.Fuerza)
