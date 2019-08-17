/* There are 2 sorted arrays A and B of size n each. 
Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n). 
The complexity should be O(log(n)). */
const median = (arr, n) => {
  if (n % 2 === 0) {
    return (arr[n / 2] + arr[n / 2 - 1]) / 2;
  } else {
    return arr[n / 2];
  }
};

const getMedian = (arr1, arr2, n) => {
  if (n <= 0) {
    return -1;
  }
  if (n === 1) {
    return (arr1[0] + arr2[0]) / 2;
  }
  if (n === 2) {
    return (Math.max(arr1[0], arr2[0]) + Math.min(arr1[1], arr2[1])) / 2;
  }

  const firstMedian = median(arr1, n);
  const secondMedian = median(arr2, n);

  if (firstMedian === secondMedian) {
    return firstMedian;
  }

  if (firstMedian < secondMedian) {
    if (n % 2 === 0) {
      return getMedian(arr1 + n / 2 - 1, arr2, n - n / 2 + 1);
    }
    return getMedian(arr1 + n / 2, arr2, n - n / 2);
  }

  if (n % 2 === 0) {
    return getMedian(arr2 + n / 2 - 1, arr1, n - n / 2 + 1);
  }
  return getMedian(arr2 + n / 2, arr1, n - n / 2);
};
