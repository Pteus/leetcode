/**
 * @param {string[]} strs
 * @return {string[][]}
 */
function groupAnagrams(strs) {
  const res = new Map();

  for (let s of strs) {
    const count = new Array(26).fill(0);
    for (let c of s) {
      count[c.charCodeAt(0) - "a".charCodeAt(0)] += 1;
    }
    const key = count.join(",");

    if (!res.has(key)) {
      res.set(key, []);
    }
    res.get(key).push(s);
  }

  return Array.from(res.values());
}

console.log("Test 1: Basic Case");
console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
// Expected output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

console.log("\nTest 2: Empty Array");
console.log(groupAnagrams([]));
// Expected output: []

console.log("\nTest 3: All Anagrams");
console.log(groupAnagrams(["abc", "bca", "cab", "bac", "acb", "cba"]));
// Expected output: [["abc", "bca", "cab", "bac", "acb", "cba"]]

console.log("\nTest 4: No Anagrams");
console.log(groupAnagrams(["hello", "world", "python", "java"]));
// Expected output: [["hello"], ["world"], ["python"], ["java"]]

console.log("\nTest 5: Single String");
console.log(groupAnagrams(["test"]));
// Expected output: [["test"]]
