class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target
   * @return {number[]}
   */
  twoSum(nums, target) {
    const map = new Map(); // <num, index>

    for (let i = 0; i < nums.length; i++) {
      const num = nums[i];

      const diff = target - num;
      if (map.has(diff)) {
        return [map.get(diff), i];
      }

      map.set(num, i);
    }

    return [];
  }
}

const solution = new Solution();

// Test cases
console.log(solution.twoSum([2, 7, 11, 15], 9)); // Expected: [0, 1]
console.log(solution.twoSum([3, 2, 4], 6)); // Expected: [1, 2]
console.log(solution.twoSum([3, 3], 6)); // Expected: [0, 1]
console.log(solution.twoSum([1, 2, 3, 4], 8)); // Expected: []
