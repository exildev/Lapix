const path = require('path');
const url = require('url');
var utils = {
    load: function(c, u, p, o ){
        c.loadURL(url.format({
            pathname: u,
            protocol: p+':',
            search: (o?o:''),
            slashes: true
        }));
    },
    loadFile: function(c, f, o){
        this.load(c, path.join(__dirname, f), 'file', o);
    }
};
module.exports = utils;
