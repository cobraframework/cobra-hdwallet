from cobra_hdwallet import HDWallet

hdWallet = HDWallet()


def test_generate_mnemonic():

    enMnemonic = hdWallet.generate_mnemonic('english')

    enCheck = hdWallet.check_mnemonic(enMnemonic, 'english')

    assert enCheck

    jpMnemonic = hdWallet.generate_mnemonic('japanese')

    jpCheck = hdWallet.check_mnemonic(jpMnemonic, 'japanese')

    assert jpCheck


def test_create_hdwallet():

    mnemonic = hdWallet.generate_mnemonic()

    created = hdWallet.create_hdwallet(mnemonic, 'password')

    assert len(created["private_key"]) == 64

    assert hdWallet.check_mnemonic(created["mnemonic"])


