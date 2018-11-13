/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
  var map = {};
  var output = {};
  var temp, min;
  for (let i = 0; i < list1.length; i++){
    map[list1[i]] = i;
  }
  for (let j = 0; j < list2.length; j++) {
    if (map[list2[j]] !== undefined) {
      temp = map[list2[j]] + j;
      min = Math.min(...Object.values(output));
      if (temp < min) {
        output = {};
        output[list2[j]] = temp;
      } else if (temp === min) {
        output[list2[j]] = temp;
      }
    }  
  }
  return Object.keys(output);
};