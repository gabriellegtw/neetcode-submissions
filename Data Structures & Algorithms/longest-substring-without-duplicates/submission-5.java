class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l = 0;
        int r = 1;
        int length = 1;
        int maxLength = 0;

        if (s.length() == 0) {
            return 0;
        }

        if (s.length() == 1) {
            return 1;
        }

        HashSet<Character> lst = new HashSet<>();
        lst.add(s.charAt(l));

        while (r < s.length()) {
            if (lst.contains(s.charAt(r))) {
                maxLength = Math.max(maxLength, length);
                length = 1;
                l += 1;
                r = l + 1;
                lst.clear();
                lst.add(s.charAt(l));
            } else {
                lst.add(s.charAt(r));
                length += 1;
                r += 1;
                maxLength = Math.max(maxLength, length);
            }
        }

        return maxLength;
    }
}
