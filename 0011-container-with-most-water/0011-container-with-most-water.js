var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let max_container = -Infinity;

  while (right > left) {
    let isRightShort = height[left] - height[right] > 0;
    let min_height = Math.min(height[right], height[left]);
    let width = right - left;
    let area = min_height * width;
    if (max_container < area) {
      max_container = area;
    }
    if (isRightShort) {
      right--;
    } else {
      left++;
    }
  }
  return max_container;
};