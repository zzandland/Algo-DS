/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  // if no rows return empty array;
  if (numRows === 0) {
    return [];
  }
  // make output array
  var output = [];
  // make first row array that contains 1 as an element
  var firstRow = [1];
  // push the firstRow into the output
  output.push(firstRow);
  // height is assigned to numRows
  var height = numRows;
  
  // recursive call function that takes current row and height
  var recurseFunc = function(currentRow, height) {
    // BASE CASE
    if (height === 0) return ;
    // make an empty array that will be pushed as the next row
    var newRow = [];
    // iterate the current row but iterate to an index that equals the length of the array
    for (var i = 0; i <= currentRow.length; i++) {
      // previousIndex value can be either as it is, or 0 if it is undefined
      var previousIndex = currentRow[i - 1] === undefined ? 0 : currentRow[i - 1];
      // currentIndex value can be either as it is, or 0 if it is undefined
      var currentIndex = currentRow[i] === undefined ? 0 : currentRow[i];
      // add the two index value as a new number
      var newNumber = previousIndex + currentIndex;
      // to the next row array push the new number
      newRow.push(newNumber);
    }

    // push the next row array into the output
    output.push(newRow);
    // invoke the recursive call function with a copy of next row array as the current row and height decremented
    recurseFunc(newRow.slice(), height - 1);
  
    // PREVIOUS EC -> return;
    return ;
  }
  
  // invoke the recursive call function with first row array and height as the parameter
  recurseFunc(firstRow, height - 1);

  // return the output array 
  return output;
};