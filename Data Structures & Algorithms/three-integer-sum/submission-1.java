class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> outer = new ArrayList<List<Integer>>();

        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int l = i + 1;
            int r = nums.length - 1;

            // So there are no duplicate triplets
            // There will be duplicate triplets if you have the same starting point
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            while (l < r) {
                if (nums[l] + nums[r] + nums[i] == 0) {
                    List<Integer> inner = new ArrayList<>();

                    inner.add(nums[l]);
                    inner.add(nums[r]);
                    inner.add(nums[i]);

                    outer.add(inner);

                    // Skip duplicates for the left pointer (l)
                    while (l < r && nums[l] == nums[l + 1]) {
                        l++;
                    }

                    // Skip duplicates for the right pointer (r)
                    while (l < r && nums[r] == nums[r - 1]) {
                        r--;
                    }
                    
                    l++;
                    r--;
                } else if (nums[l] + nums[r] + nums[i] < 0) {
                    l++;
                } else {
                    r--;
                }
            }

        }
        return outer;
    }
}
