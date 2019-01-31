from cobra_hdwallet import HDWallet

# init HDWallet
hdWallet = HDWallet()

# Generate seed
mnemonic = hdWallet.generate_mnemonic("english")

# check seed it is nor required
if not hdWallet.check_mnemonic(mnemonic, "english"):

    exit()

# Create HDWallet by seed.
enHDWallet = hdWallet.create_hdwallet(mnemonic, "password")

# You can create without seed
# withOutSeed = hdWallet.create_hdwallet("Meheret Tesfaye", "meherett")
# print(withOutSeed)

# Get HDWallet from private key
# example = bc42cee69a730913a84df8b70eee15517c0b56e8c8cc36ba3d11bbad91ee5456
# hdWallet.hdwallet_from_private(example)
pvHDWallet = hdWallet.hdwallet_from_private(enHDWallet["private_key"])

if enHDWallet["private_key"] == pvHDWallet["private_key"]:

    if enHDWallet["address"] == pvHDWallet["address"]:

        print(enHDWallet)

        print(pvHDWallet)
