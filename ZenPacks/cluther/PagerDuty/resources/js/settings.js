(function(){
    Ext.onReady(function(){
        var router = Zenoss.remote.PagerDutyRouter;

        Ext.define('cluther.pagerduty.SettingsPanel', {
            extend: 'Ext.form.Panel',
            alias: 'widget.cluther-pagerduty-settings-panel',
            title: 'PagerDuty Settings',
            defaults: {
                listeners: {
                    specialkey: function(field, event) {
                        if (event.getKey() == event.ENTER) {
                           field.up('form').submit();
                        }
                    }
                }
            },
            items: [{
                fieldLabel: 'PagerDuty API Access Key',
                labelWidth: 200,
                name: 'api_access_key',
                xtype: 'textfield'
            }],
            dockedItems: [{
                dock: 'bottom',
                xtype: 'toolbar',
                ui: 'footer',
                items: [{
                    text: 'Save',
                    handler: function() {
                        this.submit();
                    }
                }]
            }],
            onRender: function() {
                this.callParent(arguments);
                this.load();
            },
            load: function() {
                router.loadSettings({}, function(result) {
                    this.getForm().setValues(result.data);
                }, this);
            },
            submit: function() {
                router.submitSettings(this.getForm().getValues());
            }
        });

        var settings = Ext.create(cluther.pagerduty.SettingsPanel, {
            renderTo: 'pagerduty-settings'
        });

    }); // End Ext.onReady.
})(); // End closure.
