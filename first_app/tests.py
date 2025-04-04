from http.client import responses
import datetime

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from first_app.models import *


class IndexPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('')
    def test_index_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "1")

    def test_index_context(self):
        self.assertEqual(self.response.context["pages"], 7)
        self.assertEqual(self.response.context["name"], "index")


class CalcPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/calc/')

    def test_calc_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["pagename"], "calc")

    def test_simple_calc_success1(self):
        self.response = self.client.post("/calc/?a=1&b=2")
        print(self.response)
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["a"],1)
        self.assertEqual(self.response.context["b"],2)
        self.assertEqual(self.response.context["res"],3)

    def test_simple_calc_success(self):
        self.response = self.client.post("/calc/?a=564786&b=76999546")
        print(self.response)
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["a"],564786)
        self.assertEqual(self.response.context["b"],76999546)
        self.assertEqual(self.response.context["res"],77564332)

    def test_invalid_post(self):
        self.response = self.client.post('/calc/?a=dfhhshj&b=1')
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["error"], 1)


class ExpressionPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/expression/')

    def test_expression_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["pagename"], "exp")

    def test_expression_history_response(self):
        self.response = self.client.get('/history/')
        self.assertEqual(self.response.context["pagename"], "history")

    def test_history_add1(self):
        record = History(expression="50+50-36-84", result=-20)
        record.save()
        self.response = self.client.get('/history/')
        history = self.response.context["comment_history"]
        last_record = history.last()
        self.assertEqual(last_record.expression,"50+50-36-84")
        self.assertEqual(last_record.result,-20)


class StringPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/str2words/')

    def test_stringInput_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["pagename"], "strInput")

    def test_string_history_response(self):
        self.response = self.client.get('/str_history/')
        self.assertEqual(self.response.context["pagename"], "strHistory")

    def test_StrHistory_add1(self):
        self.client.post("/str2words/", data={"string": "string string erh 53"})
        self.response = self.client.get('/str_history/')
        history = self.response.context["history"]
        last_record = history.last()
        self.assertEqual(last_record.wordCount, 3)
        self.assertEqual(last_record.numCount, 1)
        self.assertEqual(last_record.wordArr, "string string erh")
        self.assertEqual(last_record.numArr, "53")
        self.assertEqual(last_record.user, "AnonymousUser")

    def test_StrHistory_add2(self):
        self.client.post("/str2words/", data={"string": ""})
        self.response = self.client.get('/str_history/')
        history = self.response.context["history"]
        last_record = history.last()
        self.assertEqual(last_record.wordCount, 0)
        self.assertEqual(last_record.numCount, 0)
        self.assertEqual(last_record.wordArr, "")
        self.assertEqual(last_record.numArr, "")
        self.assertEqual(last_record.user, "AnonymousUser")


class TimePage(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/time/')

    def test_time_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.context["pagename"], "time")
        self.assertIn("date", self.response.context)
        self.assertIn("time", self.response.context)

    def test_time_context(self):
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(self.response.context["date"], date_time_str[0:10])
        self.assertEqual(self.response.context["time"], date_time_str[11::])