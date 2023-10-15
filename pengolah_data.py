def main():
    print('=' * 25)
    print('Menu Data')
    print('1. Sorting Data')
    print('2. Lenght Data')
    print('3. Maximum Data')
    print('4. Minimum Data')
    print('5. Average Data')
    print('=' * 25)
    hitung()

def hitung(operasi, data):
    if operasi == 1:
        return sorted(data)
    elif operasi == 2:
        return len(data)
    elif operasi == 3:
        return max(data)
    elif operasi == 4:
        return min(data)
    elif operasi == 5:
        if len(data) == 0:
            return None
        return sum(data) / len(data)
    else:
        return 'Tidak Valid'

if __name__ == '__main__':
    main()