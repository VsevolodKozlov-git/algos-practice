"""
class Solution {
    private int count = 0;
    public int dieSimulator(int n, int[] rollMax) {
        dfs(n, rollMax, -1);
        return count;
    }

    private void dfs(int n, int[] rollMax, int last) {
        if (n == 0) {
            count++;
            return;
        }
        for (int i = 1; i <= 6; i++) {
            if (i == last) {
                continue;
            }
            for (int j = 1; j <= rollMax[i - 1] && n - j >= 0; j++) {
                dfs(n - j, rollMax, i);
            }
        }
    }
}
"""