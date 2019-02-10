# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    @staticmethod
    def job():
    	from datetime import datetime
    	from api.models import AliveToken
    	alive_tokens = AliveToken.objects.raw("SELECT * FROM api_alivetoken WHERE api_alivetoken.active = True")
    	for t in alive_tokens:
    		if t.end_at.replace(tzinfo=None) < datetime.now().replace(tzinfo=None):
    			t.delete()

    def ready(self):
    	import schedule
    	import time
    	schedule.every(1).minutes.do(ApiConfig.job)
    	# while True:
    	# 	schedule.run_pending()
    	# 	time.sleep(1)