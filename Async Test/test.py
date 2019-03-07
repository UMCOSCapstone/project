from multiprocessing import Pool

def sendData():
    time.sleep(2)
    print("Done Sleeping")

pool = Pool(processes=1)              # Start a worker processes.
result = pool.apply_async(sendData, [], callback)
