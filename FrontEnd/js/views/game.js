export function renderGame(container, method) {
    const rows = 6;
    const cols = 7;
    let currentPlayer = 1;
    let board = Array(rows).fill().map(() => Array(cols).fill(0));

    function createBoard() {
        let boardHTML = '<div class="game-board">';
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                boardHTML += `<div class="cell" data-row="${row}" data-col="${col}"></div>`;
            }
        }
        boardHTML += '</div>';
        return boardHTML;
    }

    function handleCellClick(event) {
        const col = parseInt(event.target.dataset.col);
        if (!isValidMove(col)) return;

        const row = getLowestEmptyRow(col);
        makeMove(row, col);
        updateBoard();
    }

    function isValidMove(col) {
        return board[0][col] === 0;
    }

    function getLowestEmptyRow(col) {
        for (let row = rows - 1; row >= 0; row--) {
            if (board[row][col] === 0) return row;
        }
        return -1;
    }

    function makeMove(row, col) {
        board[row][col] = currentPlayer;
        currentPlayer = currentPlayer === 1 ? 2 : 1;
    }

    function updateBoard() {
        const cells = container.querySelectorAll('.cell');
        cells.forEach(cell => {
            const row = parseInt(cell.dataset.row);
            const col = parseInt(cell.dataset.col);
            cell.className = 'cell';
            if (board[row][col] === 1) cell.classList.add('player1');
            if (board[row][col] === 2) cell.classList.add('player2');
        });
    }

    function handleCellHover(event) {
        const col = parseInt(event.target.dataset.col);
        const cellsInColumn = container.querySelectorAll(`.cell[data-col="${col}"]`);
        cellsInColumn.forEach(cell => cell.classList.add('hovered-column'));
    }

    function handleCellHoverOut(event) {
        const col = parseInt(event.target.dataset.col);
        const cellsInColumn = container.querySelectorAll(`.cell[data-col="${col}"]`);
        cellsInColumn.forEach(cell => cell.classList.remove('hovered-column'));
    }

    container.innerHTML = `
        <h1 class="title">Connect Four</h1>
        ${createBoard()}
    `;

    const cells = container.querySelectorAll('.cell');
    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
        cell.addEventListener('mouseenter', handleCellHover);
        cell.addEventListener('mouseleave', handleCellHoverOut);
    });
}
