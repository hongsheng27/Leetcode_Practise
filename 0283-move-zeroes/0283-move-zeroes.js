var moveZeroes = function (nums) {
  let low = 0;
  let high = low + 1;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[low] !== 0) {
      low++;
      high++;
    } else {
      if (nums[high] !== 0) {
        [nums[low], nums[high]] = [nums[high], nums[low]];
        low++;
      }
      high++;
    }
  }
  return nums;
};