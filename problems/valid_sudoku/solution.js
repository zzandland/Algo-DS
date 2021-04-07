/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const subBoxCheck = (y, x) => {
        let seen = new Array(9).fill(false);
        for (let i = 0; i < 3; ++i) {
            for (let j = 0; j < 3; ++j) {
                if (board[y+i][x+j] != '.') {
                    if (seen[parseInt(board[y+i][x+j], 10)]) return false;
                    seen[parseInt(board[y+i][x+j], 10)] = true;
                }
            }
        }
        return true;
    }
    for (let i = 0; i < 9; ++i) {
        let seenHor = new Array(9).fill(false);
        let seenVer = new Array(9).fill(false);
        for (let j = 0; j < 9; ++j) {
            if (board[i][j] != '.') {
                if (seenHor[parseInt(board[i][j], 10)]) return false;  
                seenHor[parseInt(board[i][j], 10)] = true;
            }
            if (board[j][i] != '.') {
                if (seenVer[parseInt(board[j][i], 10)]) return false;  
                seenVer[parseInt(board[j][i], 10)] = true;
            }
        }
    }
    let fail = false;
    [0, 3, 6].forEach(y => {
        [0, 3, 6].forEach(x => {
            if (!subBoxCheck(y, x)) {
                fail = true;
                return;
            }
        })
        if (fail) return;
    })
    return !fail;
};