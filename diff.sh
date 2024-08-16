#!/bin/bash

# Capture a saída do comando git diff diretamente em uma variável
diff_string=$(git diff)

# Execute o script gitai.py passando a string do diff como argumento
python3 gitai.py --diff_string "$diff_string"