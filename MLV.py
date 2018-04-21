import urllib.request as ur, multiprocessing
from threading import Thread
th = 0
b = input('>>>').split()
def func(b, th):
    def thed(i, b, th):
        if "-p" in b:
                print("2")
                ur.install_opener(ur.build_opener(
                   ur.ProxyHandler({b[b.index("-p") + 1].split("/")[0]: b[b.index("-p") + 1].split("/")[1]})))
        while i != (int(b[3]) // th):
            try:
                ur.urlopen(b[1])
                i += 1
                print('Views: +1')
            except:
                print('Some problem')
                pass
    thread = (Thread(target=thed, args=[0, b, th]) for j in range(th))
    for pp in thread:
        pp.start()
    for pp in thread:
        pp.join()
    if int(b[3]) - (int(b[3]) // th) * th != 0:
        for ij in range(int(b[3]) - (((int(b[3]) // th)) * th)):
            try:
                ur.urlopen(b[1])
                print('Views: +1')
            except:
                print('Some problem')
                pass
    else:
        raise SystemExit
def contorl(b, th):
    if th >= 95:
        print('Too much threads!')
        raise SystemExit
    if int(b[3]) >= 15988:
        print('Too much views!')
        raise SystemExit
    if (int(b[3]) + th) == 0:
        print("WTF?")
        raise SystemExit
    if "-th" not in b:
        th = multiprocessing.cpu_count()
    if "-th" in b:
        th = int(b[(b.index("-th") + 1)])
    func(b, th)
if __name__ == '__main__':
    contorl(b, th)