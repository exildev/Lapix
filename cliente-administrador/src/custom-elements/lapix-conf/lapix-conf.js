Polymer({
    is: 'lapix-conf',
    properties: {
        host: {
            type: String,
            notify: true,
            value: function() {
                return lapix.conf.get('host');
            }
        }
    },
    setHost: function (e) {
        lapix.conf.set('host', this.$.ihost.value);
    }
});
