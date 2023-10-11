def urutan_data(data):
    return sorted(data)

def panjang_data(data):
    return len(data)

def maksimum_data(data):
    return max(data)

def minimum_data(data):
    return min(data)

def ratarata_data(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)