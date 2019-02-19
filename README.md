<p align="center">
    <img src="file:///home/meheret/PycharmProjects/cobra-hdwallet/hdwallet.png">
</p>

# Cobra-HDWallet <a href="http://cobraframework.github.io" style="margin-top: 10px;">![Cobra](https://img.shields.io/badge/Cobra-Framework-EB1D25.svg?url=https://cobraframework.github.io&style=for-the-badge&colorA=0E1626&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAzCAYAAADRlospAAAACXBIWXMAAAsSAAALEgHS3X78AAAD90lEQVRogdVaO1LjQBDtVW2OA8XCkVK8J0A3wDdYE2+ATrBrbmDSjcwN7BuIbEOTKrIVbKQAog3ZatcbMWp69ENY4lW5/NFY0//pj768vLzQqZAHYUREez9L931t+aEM5EE4JaIFEc2J6MK6dCCiJ/zGn9f86sJY7wzkQTghogiEXylLHgUzNm79LF222a83BiDtJaR9VrGUGZhWrLnzszRuuu/X9qSWYRH+veFfjNls2B+IaCY0NW2zf2cGYCqrFoQ/W7a+E/fi+9xgzaINHZ0YyIMwhtSrTEVipjkpBMFmd0dEEz9Ln9rQ0oqBPAhnkKLLCavwJw/C336W/lTWsNMneJd7TmBmavht7MR5ELLEf3Ug3MY/IkqJKPazlAm2iSQjfUsrsSWsW7yvbC3VMgAn3dRI3ThlAkntqCy9OWzbmNwW76zNhAnCPhHWXiFaJXgR7rOSJlbJAEwmqbD1ezhl4rhu32sCv7nBTz+I6C8I49cEe+0MU8o9ptKMnAzUEP/AEu1yclqnM5tHghN552fpylpjrrPE11X3UxmAtPYK8c8gfNOWcAczhtCpjFKWz7Gw5q7o5GJgp9g8Ex/JGP6RyIOQNXQJf4g0JjyF+OUYiAcW2JvpSUy0slFiAPYpQ+VQxBNMyvjGBYJACVIDmsMshyDeANnpAV9vUFMUKBjAhUvx/wc7OgwIm4aSkG0NaClsq8TqA2ETfY7o9coAnEMWH/d9ln7vAaLP1rpF4QtGA5qkx2A6NuzTnrXAKUfBgMwCH4d0XAdkulLJQC8nbZ9QBHqk2UPslylDbXI2EA7WtmxGE0+rQZtklwNBBpWZh1TWxvNIiddw1IDML8bmvFWYvUnmPhs+GwNv/NVDRVS5aEQ4F6Q8eYrNy0WjAEpciZ2nhCbX4qHxpmd01AASNhk6tcWjY4BPZ+PE8uAaFQOObJmLfXIxcKXVnwNirmy9sRnQkrfGPfoTQBt6vDIAP9iKBfEYtIDqS0bGB1Ns2QeZLGDORqIFTfpFiVlqbFmNJBvfhipuHB3xg5+lxWErUwnV1oYwJXRJtHZ+qfwtMYA64E784fzUFRoOUm3PraxVtGRuiV6kjcs8CNen0AT2WLsay3K9q7nraq07m6x9oKalr/qimk5joXYac39yb1oaPRMfVxB/7QokdROaBcKrdtMtZl3van5B6isl+hlcVw05mszI6sZMW4yZWjk6tOh6HIFg83GnCY2y2RSO5ZKS2bCYceE3o3aTnkf4HDV4HGHR5Pxp9axExwF3W9xq08heGKBujxg0xT1mEa18qvPTKmDEDOm6lqFmvswS7xQMenncBj7CTsn2zZ9dvsK2zYQeB9jvzrGI6D/IKL/L4Ssv7AAAAABJRU5ErkJggg==)</a>

*It's HDWallet Generator for Ethereum blockchain.*
###### *You can paste Mnemonic(Seed) or Private-Key on Metamask/MyEtherWallet*

![GitHub](https://img.shields.io/github/license/cobraframework/cobra-hdwallet.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

## Installation

Install cobra-hdwallet
```
pip install cobra-hdwallet
```

## Usage

#### # Creating HDWallet <a href="http://cobraframework.github.io/#hdwallet" style="margin-top: 10px;">![Hdwallet](https://img.shields.io/badge/Live-Hdwallet-EB1D25.svg?style=flat-square&&colorA=0E1626&url=https://cobraframework.github.io/#hdwallet)</a>

```
from cobra_hdwallet import HDWallet

# init HDWallet
hdWallet = HDWallet()

# Generate seed
mnemonic = hdWallet.generate_mnemonic("english")

# Check seed it is not required
# if not hdWallet.check_mnemonic(mnemonic, "english"):
#     exit()

# Create HDWallet by seed and password.
# enHDWallet = hdWallet.create_hdwallet(mnemonic) # Without password
enHDWallet = hdWallet.create_hdwallet(mnemonic, "password")

# Print Generated HDWallet
print(enHDWallet)
```
```OUTPUT```

```
{
    'coin': '...',
    'name': '...', 
    'address': '...', 
    'mnemonic': '...',
    'wif': '...', 
    'finger_print': '...', 
    'chain_code': '...', 
    'private_key': '...',
    'public_key': '...', 
    'uncompressed_public_key': '...', 
    'serialized': {
        'private_key_hex': '...', 
        'public_key_hex': '...', 
        'xprivate_key_base58': '...', 
        'xpublic_key_base58': '...'
    }
}
```

#### # Get HDWallet form Private Key <a href="http://cobraframework.github.io/#hdwallet/private" style="margin-top: 10px;">![Hdwallet-Private](https://img.shields.io/badge/Live-Hdwallet_Private-EB1D25.svg?style=flat-square&&colorA=0E1626&url=https://cobraframework.github.io/#hdwallet/private)</a>

```
from cobra_hdwallet import HDWallet

# init HDWallet
hdWallet = HDWallet()

# Get HDWallet from private key
private_key = 'bc42cee69a730913a84df8b70eee15517c0b56e8c8cc36ba3d11bbad91ee5456'
pvHDWallet = hdWallet.hdwallet_from_private(private_key)

# Print HDWallet
print(pvHDWallet)
```

```OUTPUT```

```
{
    'coin': '...',
    'name': '...',
    'address': '...',
    'wif': '...',
    'finger_print': '...',
    'private_key': '...',
    'public_key': '...',
    'uncompressed_public_key': '...'
}
```

## Further help
##### # Cobra Framework
Go check out the [Cobra](http://cobraframework.github.io).

## Author
##### # Meheret Tesfaye [@meherett](http://github.com/meherett).

## Donation
##### Bitcoin *3JiPsp6bT6PkXF3f9yZsL5hrdQwtVuXXAk*
##### Ethereum *0xD32AAEDF28A848e21040B6F643861A9077F83106*