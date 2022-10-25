#andreibarbu95/python-redis-614
import redis
import os
import time

from datetime import datetime


def checkRedis (redisHost, connStr, interval):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        r = redis.StrictRedis(host=myHostname, port=6380, password=myPassword, ssl=True, socket_timeout=2)
        result = r.ping()
        print(dt_string + " "+ "Ping returned : " + str(result))
        file1= open("redis.log","a") # append modefile1.write("Today \n")file1.close()
        content = dt_string + " " + str(result)
        file1.write(content)
        file1.write("\n")
        file1.close()
        file1= open("redis.log","a") # append modefile1.write("Today \n")file1.close()
        content = dt_string + " " + str(result)
        file1.write(content)
        file1.write("\n")
        file1.close()
    except:
        print(dt_string + " "+ "Ping returned : " + "False")

if __name__ == '__main__':
  print("Starting Redis Connectivity Check:...")
  myHostname = os.getenv('REDISHOST')
  myPassword = os.environ.get('REDISPASSWORD')
  interval = os.environ.get('TIMEINTERVAL')
  while True:
    checkRedis(myHostname, myPassword, interval)
    time.sleep(int(interval))
              