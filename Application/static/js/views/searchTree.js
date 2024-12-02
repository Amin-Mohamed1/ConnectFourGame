export async function renderSearchTree(container) {
    container.innerHTML = `
        <div class="graph">
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
            console.log(data.tree);
            resultContainer.innerHTML = `<div class="tree-container"><svg id="tree-svg"></svg><div id="tooltip" class="tooltip"></div></div>`;

            drawTreeGraph(data.tree);
        } catch (error) {
            console.error('Error fetching tree:', error);
            resultContainer.innerHTML = `Error: ${error.message}`;
        }
    }

    await getTree();

    function drawTreeGraph(data) {
        const width = 2000;
        const height = 2000;
        const svg = d3.select("#tree-svg").attr("width", width).attr("height", height);
        const margin = { top: 20, right: 120, bottom: 20, left: 120 };
        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

        // Create zoom behavior
        const zoom = d3.zoom()
            .scaleExtent([0.1, 3])  // Min and max zoom scales
            .on("zoom", (event) => {
                g.attr("transform", event.transform);
            });

        svg.call(zoom);  // Apply zoom behavior to the svg

        const root = d3.hierarchy(data, d => d.children);

        // Create a tree layout
        const treeLayout = d3.tree().size([innerWidth, innerHeight]);
        treeLayout(root);

        // Draw links (paths between nodes)
        const link = g.selectAll(".link")
            .data(root.links())
            .enter()
            .append("path")
            .attr("class", "link")
            .attr("d", d3.linkVertical()
                .x(d => d.x)
                .y(d => d.y));

        // Draw nodes
        const node = g.selectAll(".node")
            .data(root.descendants())
            .enter()
            .append("g")
            .attr("class", "node")
            .attr("transform", d => `translate(${d.x},${d.y})`);

        // Add circles to nodes
        node.append("circle")
            .attr("r", 5);

        // Add text to nodes
        node.append("text")
            .attr("dy", -10)
            .style("text-anchor", "middle");

        // Tooltip functionality
        const tooltip = d3.select("#tooltip");

        node.on("mouseover", function(event, d) {
            tooltip
                .style("visibility", "visible")
                .text(`Value: ${d.data.value}, Col: ${d.data.best_child_column}`)
                .style("left", `${event.pageX + 5}px`)
                .style("top", `${event.pageY - 28}px`);
        })
        .on("mousemove", function(event) {
            tooltip
                .style("left", `${event.pageX + 5}px`)
                .style("top", `${event.pageY - 28}px`);
        })
        .on("mouseout", function() {
            tooltip.style("visibility", "hidden");
        });
    }
}
