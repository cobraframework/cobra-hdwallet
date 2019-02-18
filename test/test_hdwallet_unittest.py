# from cobra_hdwallet import HDWallet
# from unittest import TestCase
#
#
# class UnittestHDWallet(TestCase, HDWallet):
#
#     def test_generate_mnemonic(self):
#
#         enMnemonic = self.generate_mnemonic('english')
#
#         enCheck = self.check_mnemonic(enMnemonic, 'english')
#
#         self.assertTrue(enCheck)
#
#         jpMnemonic = self.generate_mnemonic('japanese')
#
#         jpCheck = self.check_mnemonic(jpMnemonic, 'japanese')
#
#         self.assertTrue(jpCheck)
#
#     def test_create_hdwallet(self):
#
#         mnemonic = self.generate_mnemonic()
#
#         created = self.create_hdwallet(mnemonic, 'password')
#
#         self.assertEqual(len(created["private_key"]), 64)
#
#         self.assertTrue(self.check_mnemonic(created["mnemonic"]))
#
#     def test_hdwallet_form_private(self):
#
#         mnemonic = self.generate_mnemonic()
#
#         created = self.create_hdwallet(mnemonic, 'password')
#
#         created_by_private = self.hdwallet_from_private(created["private_key"])
#
#         self.assertEqual(created["address"], created_by_private["address"])
#
#         self.assertEqual(created["private_key"], created_by_private["private_key"])
