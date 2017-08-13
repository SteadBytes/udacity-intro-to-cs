
def test_hash_function(func, keys, size):
    """ Calculates the distribution of a hash function across its buckets.

    Args:
        func : Hash function to test.
        keys : List of keywords.
        size (int): Number of buckets for the hash.
    Returns:
        List of int, corresponding to the number of 
            keywords mapped to each bucket by the has fucntion.
    """
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)

    return results
