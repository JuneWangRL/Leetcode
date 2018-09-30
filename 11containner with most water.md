题目：

https://leetcode.com/problems/container-with-most-water/description/

```java
class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int maxvalue=0;
        while (i<j){
            maxvalue=Math.max(maxvalue,(int)(j-i)*Math.min(height[j],height[i]));
            if(height[i]<height[j]){
                i++;
            }
            else {
                j--;
            }
        }
        return maxvalue;
    }

}
```