var characterReplacement = function (s, k) {
  let left = 0;
  let right = 0;
  let max_length = -Infinity;
  let counter = {};
  let maxFreq = 0;
  counter[s[right]] = 1;
  while (right < s.length) {
    maxFreq = Math.max(maxFreq, counter[s[right]]);
    let subStrLength = right - left + 1;

    if (subStrLength - maxFreq <= k) {
      max_length = Math.max(max_length, subStrLength);
      right++;
      counter[s[right]] = counter[s[right]] + 1 || 1;
    } else {
      counter[s[left]]--;
      left++;
    }
  }

  return max_length;
};