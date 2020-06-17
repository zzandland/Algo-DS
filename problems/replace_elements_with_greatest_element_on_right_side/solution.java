class Solution {
    public int[] replaceElements(int[] arr) {
         if (arr.length >= 3){
             int i = 0;
             int max, j, rev;
             while (i < arr.length - 1){
                 max = 0;
                 rev = 1;
                 j = i + 1;
                 while (j <= (arr.length - rev)){
                     if (arr[j] > max)
                         max = arr[j];
 
                     if (arr[arr.length-rev] > max)
                         max = arr[arr.length-rev];
                     rev ++;
                     j++;
                 }
                 arr[i] = max;
                 i++;
             }
             arr[arr.length-1] = -1;
         } else if (arr.length == 2){
             arr[0] = arr[1];
             arr[1] = -1;
         } else if (arr.length == 1){
             arr[0] = -1;
    } else {
        return null;
    }
        return arr;
    }  
}