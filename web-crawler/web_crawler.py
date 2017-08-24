import urllib.request


def get_page(url):
    try:
        f = urllib.request.urlopen(url)
        page = f.read()
        f.close()
        return page.decode('utf-8')
    except:
        return ""
    return ""


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None


def add_page_to_index(index, url, content):
    keywords = content.split()
    for word in keywords:
        add_to_index(index, word, url)


def crawl_web(seed, max_length):
    tocrawl = [seed]
    crawled = []
    index = {}
    # Holds list of outlinks for each URL
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(index) < max_length:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def is_reciprocal(graph, source, destination, k):
    """ Returns wheter a reciprocal link is present
    between source->destination, within path distance k.

    Args:
        graph (dict) = Graph to traverse
        source = node in graph (dict key) to start from
        destination = node in graph (dict key) as path destination
        k = maximum path distance to traverse.
    Returns:
        Bool
    """
    if k == 0:
        if destination == source:
            return True
        return False
    if source in graph[destination]:
        return True
    for node in graph[destination]:
        # decrease k as each recursion is one more 'hop'
        if is_reciprocal(graph, source, node, k - 1):
            return True
    return False


def compute_ranks(graph, k):
    d = 0.8  # damping factor
    numloops = 10  # number of times through relaxation

    ranks = {}
    # Initialize ranks
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            rank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal(graph, node, page, k):
                        rank += d * ranks[node] / len(graph[node])
            newranks[page] = rank
        ranks = newranks
    return ranks


def lucky_search(index, ranks, keyword):
    """Returns the URL most likely to be the best site for a given keyword.
    If the keyword does not appear in the index, returns none.

    Args:
        index (dict): Index of keywords->urls from crawl_web()
        ranks (dict): Url rankings produced by compute_ranks()
        keyword (string): Keyword to search for.
    Returns:
        String, URL of highest ranking site for keyword.abs
        None, if keyword is not present in index.
    """
    urls = lookup(index, keyword)
    if not urls:
        return None
    top_rank = urls[0]
    for url in urls:
        if ranks[url] > ranks[top_rank]:
            top_rank = url
    return top_rank


def ordered_search(index, ranks, keyword):
    """Returns an rank-ordered list of all the URLs that match the given keyword.
     If the keyword does not appear in the index, returns none.

     Args:
         index (dict): Index of keywords->urls from crawl_web()
         ranks (dict): Url rankings produced by compute_ranks()
         keyword (string): Keyword to search for.
     Returns:
         List, URL's matching keyword, ordered by rank.
         None, if keyword is not present in index.
     """
    urls = lookup(index, keyword)
    if not urls:
        return None
    return ranks_quicksort(ranks, urls)


def ranks_quicksort(ranks, urls):
    if not urls or len(urls) <= 1:
        return urls
    pivot = ranks[urls[0]]
    lower = []
    greater = []
    for url in urls[1:]:
        if ranks[url] <= pivot:
            lower.append(url)
        else:
            greater.append(url)
    return ranks_quicksort(ranks, greater) + [urls[0]] + ranks_quicksort(ranks, lower)


index, graph = crawl_web(
    'https://docs.python.org/3/', 500)
ranks = compute_ranks(graph, 2)

print(ordered_search(index, ranks, 'for'))
