import urllib3
import time
import threading

# http = urllib3.PoolManager(num_pools=10)
proxy = urllib3.ProxyManager('http://proxy_server:port_number/')
destURLs = ["https://www.baidu.com", "https://www.google.com", "https://www.baidu.com", "https://www.google.com" ]

# sequence request
startTime = time.time()
for url in destURLs:
    r = proxy.request('GET', url)
    print(r.status)
endTime = time.time() - startTime
print("%.2f"% endTime)

# threading requests
def http_request(url):
    http=proxy.request('GET',url)
    threads.append(http.status)
    if len(threads) == 6:
        endTime = time.time() - startTime
        print("%.2f" % endTime)
        print(threads)

startTime = time.time()
threads = []
for url in destURLs:
    thread = threading.Thread(target=http_request,args=(url,))
    thread.start()
    # thread.join() // will be sequence mode
