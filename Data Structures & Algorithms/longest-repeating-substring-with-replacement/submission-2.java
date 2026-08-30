class Solution {
    public int characterReplacement(String s, int k) {
        int l = 0;
        int maxLength = 1;
        int maxf = 0;

        HashMap<Character, Integer> lst = new HashMap<>();

        if (s.length() == 0) {
            return 0;
        }

        for (int i = 0; i < s.length(); i++) {
            lst.put(s.charAt(i), lst.getOrDefault(s.charAt(i), 0) + 1);
            maxf = Math.max(maxf, lst.get(s.charAt(i)));

            while ((i - l + 1) - maxf > k) {
                lst.put(s.charAt(l), lst.get(s.charAt(l)) - 1);
                l++;
            }
            maxLength = Math.max(maxLength, i - l + 1);
        }
        return maxLength;
    }
}
