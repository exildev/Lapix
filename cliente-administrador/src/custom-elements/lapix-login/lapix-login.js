Polymer({
    is: "lapix-login",
    behaviors: [
        Polymer.IronA11yKeysBehavior
    ],
    properties: {
        action: {
            type: String,
            notify: true
        },
        method: {
            type: String,
            notify: true
        },
        newUrl: {
            type: String,
            notify: true
        },
        keyEventTarget: {
            type: Object,
            value: function() {
                return document.body;
            }
        }
    },
    listeners: {
        'btnlogin.tap': '_loginSubmit',
        'btnforgot.tap': '_loginForgot',
        'loginform.iron-form-response': '_onResponse',
        'loginform.iron-form-error': '_onError',
        'loginform.iron-form-presubmit': '_preSend'
    },
    keyBindings: {
        'enter:keypress': '_loginSubmit'
    },
    _loginSubmit: function() {
        this.$.loginform.submit();
    },
    _loginForgot: function() {
        console.log('forgot');
    },
    _onResponse: function(data) {
        if (window.ipc && this.newUrl) {
            window.ipc.send('go-to', {
                file: this.newUrl
            });
        } else {
            console.log('ipc o newUrl indefinido');
        }
    },
    _onError: function(e) {
        switch (e.detail.request.status) {
            case 400:
                let errorList = e.detail.request.response;
                for (let key in errorList) {
                    if (errorList.hasOwnProperty(key)) {
                        let item = this.$.inputs.querySelector('[name="' + key + '"]');
                        if (item) {
                            item.errorMessage = errorList[key][0];
                            item.invalid = true;
                        } else if (key === "error") {
                            this.$.error.textContent = errorList[key][0];
                            break;
                        }
                    }
                }
                break;
            default:
                break;
        }
    },
    _preSend: function() {
        this.$.error.textContent = "";
    }
});
