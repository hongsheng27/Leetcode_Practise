class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = new HashMap<>();
        for(String s: strs){
            int[] board = new int[26];
            for (char c: s.toCharArray()){
                board[c - 'a'] ++;
            }
            String key = Arrays.toString(board);
            res.putIfAbsent(key, new ArrayList<>());
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values());
    }
}