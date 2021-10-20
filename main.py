from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm

from dowloader import Downloader

if __name__ == '__main__':
    allLines = open("C:\\Users\\phone\\Downloads\\202110192017.txt", 'r', encoding='UTF-8').readlines()
    n = len(allLines)
    p = ThreadPoolExecutor(max_workers=2)
    bar = tqdm(total=n)
    for line in allLines:
        if len(line.strip()) == 0: continue
        d = Downloader(url=line, path="G:\\20211019")
        f = p.submit(d.run)
        f.add_done_callback(lambda _: bar.update(1))
