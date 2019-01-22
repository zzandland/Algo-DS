var leastInterval = function(tasks, n) {
  let output = 0;
  // make Hashtable <char, occurrence>
  const map = new Array(26).fill(0);
  tasks.forEach(task => {
    map[task.charCodeAt() - 'A'.charCodeAt()]++;
  });
  let count = 0;
  const max = Math.max(...map);
  for (let i = 0; i < map.length; i++) {
    if (map[i] === max) count++;
  }
  // loop until hashtable is empty
  return Math.max((n + 1) * (max - 1) + count, tasks.length);
};