const {app, BrowserWindow, ipcMain, dialog} = require('electron');
const Config = require('electron-config');
const utils = require('./main-utils.js');
const path = require('path');

 const config = new Config();
let win;
let dt;

function init() {
    const {width, height} = require('electron').screen.getPrimaryDisplay().workAreaSize;
    if(!config.has('host')){
        config.set('host', 'http://104.236.33.228:8070/');
    }
    win = new BrowserWindow({
        icon: path.join(__dirname, '../images/test tube.png'),
        width: width,
        height: height,
        show: false
    });

    utils.loadFile(win, '../login.html');
    win.once('ready-to-show', () => {
        win.show();
    });
    win.on('closed', () => {
        win = null;
    });
    dt = new BrowserWindow({
        parent: win,
        modal: true,
        icon: path.join(__dirname, '../images/test tube.png'),
        show: false,
        frame: false
    });
}

app.on('ready', init);


app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (win === null) {
        init();
    }
});

ipcMain.on('devtools', (e) => win.webContents.openDevTools());

ipcMain.on('go-to', (e, args) => utils.loadFile(win, '../'+args.file));

ipcMain.on('win-reload', () => utils.loadFile(win, '../index.html'));

ipcMain.on('dt-load', (e, args) => {
    utils.loadFile(dt,'../src/app/base/dialog-theme.html','url=../'+args.file);
    dt.show();
});

ipcMain.on('dt-close', () => dt.hide());
