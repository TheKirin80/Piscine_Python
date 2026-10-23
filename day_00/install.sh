#!/usr/bin/bash

python3.10 -y
# pour l'ex08 du day 00 il faut tqdm en 3.10
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
/usr/bin/python3.10 get-pip.py --user
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
/usr/bin/python3.10 -m pip install tqdm