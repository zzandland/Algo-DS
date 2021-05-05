func jump(nums []int) int {
    n := len(nums)
    if n < 2 { return 0 }
    i, lv, mx := 0, 0, 0
    for i < n {
        lv++;
        nxt := 0
        for ; i <= mx; i++ {
            nxt = int(math.Max(float64(nxt), float64(i + nums[i])))
            if nxt >= n - 1 { return lv }
        }
        mx = nxt
    }
    return -1
}