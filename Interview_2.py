def count_zero(string):
    count = 0
    arr = []
    for i in range(len(string)):
        if (string[i] == '0'):
            count += 1
        if (string[i] == '1'):
            arr.append(count)
            count = 0
    return max(arr)

def main():
    print(count_zero("1010110100001"))

if __name__ == '__main__':
    main()