function breadthFirstSearch(graph, startNode) {
  const visited = new Set();
  const queue = [startNode];
  const order = [];

  while (queue.length > 0) {
    const currentNode = queue.shift();
    if (!visited.has(currentNode)) {
      visited.add(currentNode);
      order.push(currentNode);

      for (const neighbor of graph[currentNode]) {
        if (!visited.has(neighbor)) {
          queue.push(neighbor);
        }
      }
    }
  }

  return order;
}

const graph = {
  A: ["B", "C"],
  B: ["A", "D", "E"],
  C: ["A", "F"],
  D: ["B"],
  E: ["B", "F"],
  F: ["C", "E", "G"],
  G: ["F"],
};

const startNode = "A";
console.log("BFS Traversal:", breadthFirstSearch(graph, startNode));
