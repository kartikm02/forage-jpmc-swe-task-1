"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
function activate(context) {
    let currentPanel = undefined;
    // The command has been defined in the package.json file
    // Now provide the implementation of the command with registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('reacticons.reacticons', () => {
        const columnToShowIn = vscode.window.activeTextEditor
            ? vscode.window.activeTextEditor.viewColumn
            : undefined;
        if (currentPanel) {
            // If we already have a panel, show it in the target column
            currentPanel.reveal(columnToShowIn);
        }
        else {
            // Otherwise, create a new panel
            currentPanel = vscode.window.createWebviewPanel('reacticons', // Identifies the type of the webview. Used internally
            'React Icons', // Title of the panel displayed to the user
            vscode.ViewColumn.Beside, // Editor column to show the new webview panel in.
            {
                enableScripts: true,
                retainContextWhenHidden: true
            });
            currentPanel.webview.html = getWebviewContent();
            // Reset when the current panel is closed
            currentPanel.onDidDispose(() => {
                currentPanel = undefined;
            }, null, context.subscriptions);
        }
        // const filePath: vscode.Uri = vscode.Uri.file(path.join(context.extensionPath, 'src', 'public', 'index.html'));
        // panel.webview.html = fs.readFileSync(filePath.fsPath,'utf8');
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
function getWebviewContent() {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>React Icons</title>
		<style>
		.full {
			height: 100vh;
			width: 100vw;
			margin: 0;
			padding: 0;
			border: 0;
			outline: none;
		}
		
		</style>
</head>
<body class="full">
    <iframe src="https://react-icons-preview.vercel.app/" class="full" sandbox="allow-scripts allow-same-origin">/>
</body>
</html>`;
}
//# sourceMappingURL=extension.js.map