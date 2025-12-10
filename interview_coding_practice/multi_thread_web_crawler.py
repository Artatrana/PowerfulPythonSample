import threading
import queue
import networkx as nx
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class WebCrawler:
    def __init__(self, urls, max_threads=5):
        self.urls = urls
        self.visited = set()
        self.graph = nx.DiGraph()
        self.queue = queue.Queue()
        self.max_threads = max_threads

        for url in urls:
            self.queue.put(url)

    def fetch_and_parse(self, url):
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
                return links
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
        return []

    def worker(self):
        while not self.queue.empty():
            url = self.queue.get()
            if url not in self.visited:
                self.visited.add(url)
                print(f"Crawling: {url}")
                links = self.fetch_and_parse(url)
                for link in links:
                    self.graph.add_edge(url, link)
                    if link not in self.visited:
                        self.queue.put(link)
            self.queue.task_done()

    def crawl(self):
        threads = []
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    def run_pagerank(self):
        pr = nx.pagerank(self.graph)
        return pr

if __name__ == "__main__":
    seed_urls = ['https://example.com']
    crawler = WebCrawler(seed_urls, max_threads=3)
    crawler.crawl()

    print("\nPageRank Scores:")
    pagerank_scores = crawler.run_pagerank()
    for url, score in pagerank_scores.items():
        print(f"{url}: {score:.4f}")
