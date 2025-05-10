var searchInsert = function(nums, target) {
  let i = 0;
  let j = nums.length - 1;

  while (i <= j) {
    let mid = Math.floor((i + j) / 2);
    if (nums[mid] === target) {
      return mid;
    } else if (target < nums[mid]) {
      j = mid - 1;
    } else {
      i = mid + 1;
    }
  }

  return i;
};