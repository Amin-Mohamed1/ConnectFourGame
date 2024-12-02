import { renderHome } from './views/home.js';
import { renderAISelection } from './views/aiSelection.js';
import { renderGame } from './views/game.js';
import { renderSearchTree } from './views/searchTree.js';
import { renderDepthAndStarter } from './views/depthAndStarter.js';

const app = document.getElementById('app');

function router() {
    const fullHash = window.location.hash || '#/';
    const [hash, queryString] = fullHash.split('?');
    const searchParams = new URLSearchParams(queryString);
    const method = searchParams.get('method');
    const depth = searchParams.get('depth');
    const starter = searchParams.get('starter');

    switch (hash) {
        case '#/':
            renderHome(app);
            break;
        case '#/ai-selection':
            renderAISelection(app);
            break;
        case '#/game':
            renderGame(app, method, depth, starter);
            break;
        case '#/search-tree':
            renderSearchTree(app);
            break;
        case '#/depth-and-starter':
            renderDepthAndStarter(app, method);
            break
        default:
            renderHome(app);
    }
}

window.addEventListener('hashchange', router);
router();