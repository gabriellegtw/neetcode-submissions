class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        HashMap<Character, Integer> s1Map = new HashMap<>();
        HashMap<Character, Integer> s2Map = new HashMap<>();
        int windowSize = s1.length();

        // Populate frequency map for s1
        for (char c : s1.toCharArray()) {
            s1Map.put(c, s1Map.getOrDefault(c, 0) + 1);
        }

        // Initialize the first window
        for (int i = 0; i < windowSize; i++) {
            char c = s2.charAt(i);
            s2Map.put(c, s2Map.getOrDefault(c, 0) + 1);
        }

        // If first window is a match, return true
        if (s1Map.equals(s2Map)) {
            return true;
        }

        // Slide the window across s2
        for (int right = windowSize; right < s2.length(); right++) {
            char rightChar = s2.charAt(right);
            char leftChar = s2.charAt(right - windowSize);

            // Add new character to window
            s2Map.put(rightChar, s2Map.getOrDefault(rightChar, 0) + 1);

            // Remove the character that goes out of the window
            if (s2Map.get(leftChar) == 1) {
                s2Map.remove(leftChar);
            } else {
                s2Map.put(leftChar, s2Map.get(leftChar) - 1);
            }

            // Check if the frequency maps match
            if (s1Map.equals(s2Map)) {
                return true; // No need for a flag, just return immediately
            }
        }

        return false; // If no match found
    }
}
