from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="cobra-hdwallet",
    version='0.1.0',
    description='It\'s HDWallet Generator for Ethereum blockchain.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Meheret Tesfaye',
    author_email='meherett@zoho.com',
    url='https://github.com/cobraframework/cobra-hdwallet',
    python_requires='>=3.5,<3.7',
    packages=['cobra_hdwallet'],
    install_requires=[
        'ecdsa==0.13',
        'two1==3.10.9',
        'base58==0.2.2',
        'pysha3==1.0.2',
        'mnemonic==0.13',
        'eth_keyfile==0.5.1'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Framework :: Cobra",
    ],
)
