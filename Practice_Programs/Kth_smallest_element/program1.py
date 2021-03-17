def kthSmallestEle(arr,n,k):
    arr.sort()
    return arr[k-1]

if __name__ == "__main__":
    arr = [12,43,21,23,4,5]
    n = len(arr)
    k = 2
    print("Kth smallest element is ",kthSmallestEle(arr,n,k))