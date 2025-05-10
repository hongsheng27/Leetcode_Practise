var isPowerOfFour = function (n) {
  if (n > 1) return isPowerOfFour(n / 4);
  return n === 1;
};