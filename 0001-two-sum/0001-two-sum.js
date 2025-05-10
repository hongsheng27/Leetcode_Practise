var twoSum = function (nums, target) {
  let counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (counter[nums[i]] !== undefined) {
      return [counter[nums[i]], i];
    }
    let complement = target - nums[i];
    counter[complement] = i;
  }

  return [];
};

