export async function renderSearchTree(container) {
    container.innerHTML = `
        <div class="main-container">
            <h1 class="title">Search Tree</h1>
            <div id="result-container">Loading...</div>
        </div>
    `;

    const resultContainer = document.getElementById('result-container');

    async function getTree() {
        try {
            const response = await fetch('/tree', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Render the tree structure in HTML
            const treeHTML = renderNode(data.tree);
            resultContainer.innerHTML = `<ul>${treeHTML}</ul>`;            
        } catch (error) {
            console.error('Error fetching tree:', error);
            resultContainer.innerHTML = `Error: ${error.message}`;
        }
    }

    // Recursive function to render a tree node
    function renderNode(node) {
        const isTerminal = node.children.length === 0;

        // Render the current node
        let nodeHTML = `
            <li>
                <div class="node">
                    <strong>Best Child Column:</strong> ${node.best_child_column} <br>
                    <strong>Column:</strong> ${node.column} <br>
                    <strong>Value:</strong> ${node.value}
                </div>
        `;

        // If the node has children, render them recursively
        if (!isTerminal) {
            nodeHTML += `<ul>`;
            for (const child of node.children) {
                nodeHTML += renderNode(child);
            }
            nodeHTML += `</ul>`;
        }

        nodeHTML += `</li>`;
        return nodeHTML;
    }

    // Call the function to fetch and render the tree
    await getTree();
}