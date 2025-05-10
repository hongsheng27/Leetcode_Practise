var evalRPN = function (tokens) {
  const operators = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
    "/": (a, b) => Math.trunc(a / b),  // truncate toward zero
  };

  const stack = [];

  for (let token of tokens) {
    if (!(token in operators)) {
      stack.push(Number(token)); // ✅ 轉成數字再 push
    } else {
      const b = stack.pop();
      const a = stack.pop();
      const res = operators[token](a, b);
      stack.push(res);
    }
  }

  return stack.pop();
};