var isPalindrome = function (s) {
  let newStr = s.toLowerCase().replace(/[^a-z0-9]+/g, "");
  let left = 0;
  let right = newStr.length - 1;

  while (right >= left) {
    if (newStr[left] === newStr[right]) {
      left++;
      right--;
    } else {
      return false;
    }
  }
  return true;
};