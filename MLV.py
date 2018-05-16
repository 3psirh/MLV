import urllib.request as ur, multiprocessing
from threading import Thread
print('''                             
@@@@@@@@@@    @@@      @@@  @@@
@@! @@! @@!   @@!      @@!  @@@
@!! !!@ @!@   @!!      @!@  !@!
!!:     !!    !!:       !: .:! 
 "      "     :;;:;;.     ?;   \n\nMLV v2.0''')
th = 0
b = ""
try:
    b = input('>>>').split()
except KeyboardInterrupt:
    print("Shutdown requested...Goodbye...")
    raise SystemExit
if "-p" in b:
    ur.install_opener(ur.build_opener(
        ur.ProxyHandler({b[b.index("-p") + 1].split("/")[0]: b[b.index("-p") + 1].split("/")[1]})))

def thed(b, count):
    i = 0
    if "-txtp" in b:
        file = open(b[b.index("-txtp") + 1], "r")
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
            print('Views: +1')
            i+=1
            print(i)
        except:
            print('Some problem')
            pass


def func(b, th):
    count = (int(b[3]) // th)
    thread = (Thread(target=thed, args=[b, count]) for j in range(th))
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
    if int(b[3]) == 0:
        print("No views!")
        raise SystemExit
    if "-th" in b:
        try:
            th = int(b[b.index("-th") + 1])
        except IndexError:
            th = multiprocessing.cpu_count()
        func(b, th)
    else:
        count = int(b[3])
        thed(b, count)
if __name__ == '__main__':
    control(b)