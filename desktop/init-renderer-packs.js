try{
    require('devtron').install();
} catch(e){
    console.warn('No se pudo cargar devtron', e);
}

try {
    window.ipc = require('electron').ipcRenderer;
} catch (e) {
    console.warn('No se pudo cargar ipcRenderer', e);
}

try {
    let Config = require('electron-config');
    window.lapix = window.lapix || {};
    window.lapix.conf = new Config();
} catch (e) {
    console.warn('No se pudo cargar electron-config', e);
}
