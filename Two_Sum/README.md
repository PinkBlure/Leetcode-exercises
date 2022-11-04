# ✨ Project's Title: Two Sums ✨

### Project Description

#### What does the function do?
* This is a function to get the two indices of a list of integers such that they add up to one target.

#### Why use Python?
* It use a symple syntax so its's easier to read and understand, beginner friendly, and has a large and active community.

#### Challenges faced while coding
* You may assume that each input would have exactly one solution
* You may not use the same element twice.

#### How to run the function
* The function ask for a list composed of integers and a integer.
* The numbers in the list are the numbers that are going to get sum in pairs.
* The integer is the target of the sum of the pair of num.
* It returns the list of the two index of the list of nums that made the sum for target given.

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### Link to the source of the exercises
* https://leetcode.com/problems/two-sum/
