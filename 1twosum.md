Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

```java
package com.company;

import java.util.ArrayList;

public class lctest {
    public int[] twoSum(int[] nums, int target) {
        int[] res=new int[2];
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            list.add(target-nums[i]);
        }
        //System.out.println(list);
        for(int i=0;i<nums.length;i++){
            Integer num=new Integer(nums[i]);
            int idx=list.indexOf(num);
            if (idx>-1&&idx!=i){
                res[0]=i;
                res[1]=idx;
                break;
            }
        }
        return res;
    }
    public static void main(String[] args){
        int[] a = {1,2,4};
        lctest b=new lctest();
        int[] s=b.twoSum(a,3);
        System.out.println(s[0]);
        System.out.println(s[1]);
    }
}
```