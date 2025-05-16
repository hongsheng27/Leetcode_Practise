class MinStack {
  constructor() {
    this.stack = [];
  }
  push(val) {
    if (this.stack.length === 0) {
      this.stack.push({ val, min: val });
    } else {
      this.stack.push({
        val,
        min: Math.min(this.stack[this.stack.length - 1].min, val),
      });
    }
  }
  pop() {
    if (this.stack.length > 0) {
      this.stack.pop();
    }
  }
  top() {
    console.log(this.stack[this.stack.length - 1]);
    return this.stack[this.stack.length - 1].val;
  }
  getMin() {
    return this.stack[this.stack.length - 1].min;
  }
}