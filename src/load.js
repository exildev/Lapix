window.Polymer = { lazyRegister: true, dom: 'shadow' };
(function() {
    if ('registerElement' in document &&
        'import' in document.createElement('link') &&
        'content' in document.createElement('template')) {
    } else {
        var e = document.createElement('script');
        e.src = './bower_components/webcomponentsjs/webcomponents-lite.min.js';
        document.head.appendChild(e);
    }
})();