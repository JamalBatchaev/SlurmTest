#Если бы мы запустили на Python скрипт, выполняющий простую задачу — спать (ну очень времязатратную!), он выглядел бы так:
import time
start = time.perf_counter()
def please_sleep(n):
    print("Sleeping for {} seconds".format(n))
    time.sleep(n)
    print("Done Sleeping")
for i in range(1,5):
   please_sleep(i)
finish = time.perf_counter()
print("Finished in {} seconds".format(finish-start))