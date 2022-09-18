class Solution {
    public boolean canPartition(int[] nums) {
        int sum=0;
        for(int n=0;n<nums.length;n++) 
            sum=sum+nums[n];
        if(sum%2 == 1) 
            return false;
        sum /= 2;
        boolean[][] t = new boolean[nums.length+1][sum+1];
        for(int i=0;i<nums.length+1;i++) 
            t[i][0] = true;
        for(int i=1;i<nums.length+1;i++){
            for(int j=1;j<sum+1;j++){
                if(nums[i-1] <= j){
                    t[i][j] = t[i-1][j-nums[i-1]] || t[i-1][j];
                }
                else{
                    t[i][j] = t[i-1][j];
                }
            }
        }
        return t[nums.length][sum];
    }
}