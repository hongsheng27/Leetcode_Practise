/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  const counter = {};
  for (let i = 0; i < nums.length; i++) {
    if (counter[nums[i]]) {
      counter[nums[i]] = 2;
    } else {
      counter[nums[i]] = 1;
    }
  }
  for (let item in counter) {
    if (counter[item] === 1) {
      return Number(item);
    }
  }
  return null;
};