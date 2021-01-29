from django.test import TestCase
from .models import *

# Create your tests here.
class templateTests(TestCase):
    def setUp(self):
        EmailTemp.objects.create(category="Tests",letter="Hello world!")
        EmailTemp.objects.create(category="Tests",letter="Goodbye!")
        Address.objects.create(address="1600 Pennsylvania Avenue, Washington, DC")

    def test_unapproved(self):
        hello = EmailTemp.objects.get(letter="Hello world!")
        goodbye = EmailTemp.objects.get(letter="Goodbye!")
        self.assertFalse(hello.approved)
        self.assertFalse(goodbye.approved)

    def test_manual_approval(self):
        hello = EmailTemp.objects.get(letter="Hello world!")
        goodbye = EmailTemp.objects.get(letter="Goodbye!")
        goodbye.approved = True
        self.assertFalse(hello.approved)
        self.assertTrue(goodbye.approved)

    def test_no_sender(self):
        hello = EmailTemp.objects.get(letter="Hello world!")
        goodbye = EmailTemp.objects.get(letter="Goodbye!")
        self.assertEqual(hello.sender, "")
        self.assertEqual(goodbye.sender, "")

    def test_case_sensitive(self):
        hello = EmailTemp.objects.get(letter="Hello world!")
        goodbye = EmailTemp.objects.get(letter="Goodbye!")
        hello.sender = "Brendan"
        goodbye.sender = "brendan"
        self.assertEqual(hello.sender, "Brendan")
        self.assertEqual(goodbye.sender, "brendan")
        self.assertNotEqual(hello.sender, goodbye.sender)

    def test_addr_conversion(self):
        addr = Address.objects.get(address="1600 Pennsylvania Avenue, Washington, DC")
        spl = addr.address.split()
        conv = ""
        for x in spl:
            x = x.replace(',', '')
            conv += x + "%20"
        conv = conv[:-3]
        self.assertEqual(conv, "1600%20Pennsylvania%20Avenue%20Washington%20DC")
    
    def tearDown(self):
        hello = EmailTemp.objects.get(letter="Hello world!")
        goodbye = EmailTemp.objects.get(letter="Goodbye!")
        hello.delete()
        goodbye.delete()
