/** @odoo-module **/

import { Message } from '@mail/components/message/message';
import { patch } from "@web/core/utils/patch";
const { onWillStart, useState } = owl;
import { useService } from "@web/core/utils/hooks";

patch(Message.prototype, 'mail/components/message/message.js', {
    setup(){
        var self = this;
        this.rpc = useService("rpc");
        this.orm = useService("orm");
        this.email_cc = false
        onWillStart(async ()=> {
            var message_id = self.props.record.message.id;
            if (message_id > 0){
                var email_cc = await self.get_email_cc(message_id);
                if(email_cc){
                    self.email_cc = email_cc;
                }
            }

        })
        this._super.apply(this, arguments);
    },

    async get_email_cc(message_id){
        var result = await this.orm.searchRead('mail.message',[['id','=',message_id]], ['email_cc'])
        if (result){
            return new Promise((resolve, reject)=>{
                if (result.length > 0){
                    resolve(result[0].email_cc);
                }
                else {
                    reject('error');
                }
            })
        }
    }
})