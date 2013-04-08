(function(){

Ext.onReady(function(){
    var store = Ext.create('Ext.data.JsonStore', {
        autoSync: true,
        fields: [{name: 'key'}, {name: 'value'}],
        proxy: {type: 'memory'},
        listeners: {
            write: function(store, operation) {
                if (!hidden_field) {
                    return;
                }

                vs = [];

                Ext.each(store.getRange(), function(record) {
                    if (record.data.key) {
                        vs.push(record.data);
                    }
                });

                hidden_field.setValue(Ext.JSON.encode(vs));
            }
        }
    });

    var hidden_field = Ext.create('Ext.form.field.Hidden', {name: 'details'});

    var row_editor = Ext.create('Ext.grid.plugin.RowEditing');

    var grid_panel = Ext.create('Ext.grid.Panel', {
        title: _t('Details'),
        height: 200,
        plugins: [row_editor],
        store: store,

        dockedItems: [{
            xtype: 'toolbar',
            store: store,
            items: [{
                text: 'Add',
                iconCls: 'icon-add',
                handler: function() {
                    store.insert(0, {key: '', value: ''});
                    row_editor.startEdit(0, 0);
                }
            }, '-', {
                itemId: 'delete',
                text: 'Delete',
                iconCls: 'icon-delete',
                handler: function(){
                    var selection = grid_panel.getView().getSelectionModel().getSelection()[0];
                    if (selection) {
                        store.remove(selection);
                        store.sync();
                    }
                }
            }]
        }],

        columns: [{
            header: _t('Key'),
            dataIndex: 'key',
            editor: { xtype: 'textfield', allowBlank: true },
            sortable: true,
            width: 200
        },{
            header: _t('Value'),
            dataIndex: 'value',
            editor: { xtype: 'textfield', allowBlank: true },
            sortable: true,
            flex: 1
        }]
    });

    Ext.define('cluther.actions.pagerduty.DetailsField', {
        extend: 'Ext.container.Container',
        alias: 'widget.cluther-actions-pagerduty-details-field',
        items: [hidden_field, grid_panel],

        initComponent: function() {
            this.callParent(arguments);

            if (this.value) {
                hidden_field.setValue(this.value);
                store.loadData(Ext.JSON.decode(this.value));
            }
        }
    });
});

})();
