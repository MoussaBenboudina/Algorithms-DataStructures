function depthFirstSearch(graph, startNode) {
  const visited = new Set();
  const order = [];

  function dfs(node) {
    if (!visited.has(node)) {
      visited.add(node);
      order.push(node);

      for (const neighbor of graph[node]) {
        if (!visited.has(neighbor)) {
          dfs(neighbor);
        }
      }
    }
  }

  dfs(startNode);
  return order;
}
