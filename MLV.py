import multiprocessing
import urllib.request as ur
from threading import Thread

print('''                             
@@@@@@@@@@    @@@      @@@  @@@
@@! @@! @@!   @@!      @@!  @@@
@!! !!@ @!@   @!!      @!@  !@!
!!:     !!    !!:       !: .:! 
 "      "     :;;:;;.     ?;   \n\nMLV v2.1''')
file = ""
try:
    b = input('>>>').split()
except KeyboardInterrupt:
    print("Shutdown requested...Goodbye...")
    raise SystemExit
if "-p" in b:
    ur.install_opener(ur.build_opener(
        ur.ProxyHandler({b[b.index("-p") + 1].split("/")[0]: b[b.index("-p") + 1].split("/")[1]})))
if "-txtp" in b:
    file = open(b[b.index("-txtp") + 1], "r")


def thed(b, count, file):
    i = 0
    while i != count:
        if i == count:
            break
        if "-txtp" in b:
            try:
                bg = file.readline(-1)
                if bg.replace('\n', '') == "":
                    file = open(b[b.index("-txtp") + 1], "r")
                    bg = file.readline(-1)
                ur.install_opener(ur.build_opener(
                    ur.ProxyHandler({bg.split(";")[0]: bg.replace('\n', '')[1]})))
            except:
                print("ERROR")
                pass
        try:
            ur.urlopen(b[1])
            i += 1
            print('Views: +1')
        except:
            print('Some problem')
            pass


def func(b, th):
    count = (int(b[3]) // th)
    print(th)
    thread = (Thread(target=thed, args=[b, count, file]) for j in range(th))
    for pp in thread:
        pp.start()
    for pp in thread:
        pp.join()
    if int(b[3]) - (int(b[3]) // th) * th != 0:
        for ij in range(int(b[3]) - ((int(b[3]) // th) * th)):
            try:
                ur.urlopen(b[1])
                print('Views: +1')
            except:
                print('Some problem')
                pass
    else:
        raise SystemExit


def control(b):
    try:
        th = int(b[b.index("-th") + 1])
    except ValueError or IndexError:
        th = multiprocessing.cpu_count()
    func(b, th)


if __name__ == '__main__':
    control(b)
