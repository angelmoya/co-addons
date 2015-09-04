# -*- encoding: utf-8 -*-

from openerp import models

class PartnerRef(models.Model):
    _inherit="res.partner"
    
    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.ref and '[' + record.ref + '] ' or ''
            try:
                name =str(name)+record.name
            except:
                name = record.name
            if record.parent_id and not record.is_company:
                name =  "%s, %s" % (record.parent_id.name, name)
            if context.get('show_address_only'):
                name = self._display_address(cr, uid, record, without_company=True, context=context)
            if context.get('show_address'):
                name = name + "\n" + self._display_address(cr, uid, record, without_company=True, context=context)
            name = name.replace('\n\n','\n')
            name = name.replace('\n\n','\n')
            if context.get('show_email') and record.email:
                name = "%s <%s>" % (name, record.email)
            res.append((record.id, name))
        return res
    