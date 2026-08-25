def countCyclicPairs(nums):
  buckets = defaultdict(list)
  res = 0
  for num in nums:
    s = str(num)
    key = s
    doubled = s + s
    for i in range(len(s)):
      key = min(key, doubled[i: i + len(s)])
    buckets[key].append(num)

  for bucket in buckets.values():
    k = len(bucket)
    res += k * (k - 1) // 2
  return res