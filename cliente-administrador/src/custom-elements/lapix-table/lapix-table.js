Polymer({
    is: "lapix-table",
    properties: {
        site: {
            type: String,
            notify: true
        },
        fullUrl: {
            type: String,
            computed: 'computeFullUrl(site)',
            notify: true
        },
        label: {
            type: String,
            notify: true
        },
        _dataSource: {
            type: Object
        },
        addUrl: String,
        search: {
            type: String,
            value: '',
            observer: 'retrieveResults'
        }
    },
    listeners: {
        'get.response': '_onGetResponse',
        'set.response': '_onSetResponse',
        'del.response': '_onDelResponse',
        'get.error': '_onGetError',
        'set.error': '_onSetError',
        'del.error': '_onDelError',
    },
    ready: function() {
        let form = this.querySelector('[form]');
        if(form){
            form._formResponse = env => {
                this.$.dialog.close();
                this.retrieveResults();
            };
        }
        this._dataSource = {
            get: (sort, page, pageSize) => {
                this.$.get.params = {
                    page: page,
                    num_page: pageSize,
                    sort_property: sort.property,
                    sort_direction: sort.direction,
                    q: this.search
                };
                this.$.get.generateRequest();
                return new Promise((resolve, reject) => {
                    this._onGetResponse = evn => {
                        this.set('_dataSource.length', evn.detail.response.count);
                        if(evn.detail.response.object_list.length > 0){
                            console.log(evn.detail.response.object_list);
                            this.addUrl = evn.detail.response.object_list[0].servicios.add;
                            resolve(evn.detail.response.object_list);
                        }else{
                            resolve([]);
                        }
                    };
                    this._onGetError = evn => {
                        console.warn('Error al consultar los datos', evn);
                        resolve([]);
                    };
                });
            },
            set: (item, property, value) => {
                let aux = JSON.parse(JSON.stringify(item));
                this.$.set.url = lapix.conf.get('host') + aux.servicios.edit;
                this.$.set.body = this.cleanParameter(aux);
                this.$.set.generateRequest();
                return new Promise((resolve, reject) => {
                    this._onSetResponse = evn => {
                        this.retrieveResults();
                        resolve(true);
                    };
                    this._onSetError = evn => {
                        console.warn('no se pudueron guardar los cambios');
                        resolve(false);
                    };
                });
            },
            length: 0
        };

    },
    cleanParameter: function(item){
        console.warn('Sobrescribe esta funcion en tu implementacion de lapix-table');
    },
    retrieveResults: function(ev){
        this.computeFullUrl(this.site);
        this.$.datatableCard.retrieveVisibleData();
    },
    computeFullUrl: function(site){
        return lapix.conf.get('host') + site;
    },
    deleteSelected: function(){
        for (let item of this.selectedItems) {
            this.$.del.url = lapix.conf.get('host') + item.servicios.delete;
            this.$.del.generateRequest();
        }
    },
    editDialogForSelected: function () {
        let item = this.selectedItems[0];
        let form = this.querySelector('[form]');
        if(form){
            let aux = JSON.parse(JSON.stringify(item));
            form.add = false;
            form.action = lapix.conf.get('host') + aux.servicios.edit;
            form.values = this.cleanParameter(aux);
            this.$.dialog.open();
        }else{
            console.warn('No has definido un formulario para este Elemento');
        }
    },
    _onDelResponse: function(){
        this.retrieveResults();
    },
    _onDelError: function(evn){
        console.warn('no se pudo eliminar el registro', evn);
    },
    _onTapAdd: function () {
        let form = this.querySelector('[form]');
        if(form){
            form.add = true;
            form.action = lapix.conf.get('host') + this.addUrl;
            console.log(form.action);
            form.values = null;
            form.reset();
            this.$.dialog.open();
        }else{
            console.warn('No has definido un formulario para este Elemento');
        }
    },
    _dismissDialog: function (evn) {
        let form = this.querySelector('[form]');
        form.submit();
    }
});
